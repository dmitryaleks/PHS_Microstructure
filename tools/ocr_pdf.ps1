<#
OCR a scanned PDF with the renderer and OCR engine built into Windows 10/11
(Windows.Data.Pdf + Windows.Media.Ocr) -- no third-party installs.

Writes UTF-8 text with one marker line per PHYSICAL page, matching the citation
convention used everywhere else in the knowledge base:

    ===== page 7 / 41 =====

Usage:  powershell -NoProfile -ExecutionPolicy Bypass -File tools\ocr_pdf.ps1 -PdfPath kb\pdfs\x.pdf -OutPath sources\ocr\x.txt
Called for every scanned document by tools\ocr_sources.py.
#>
param(
    [Parameter(Mandatory = $true)][string]$PdfPath,
    [Parameter(Mandatory = $true)][string]$OutPath,
    [int]$Width = 2400
)
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Runtime.WindowsRuntime
$null = [Windows.Storage.StorageFile, Windows.Storage, ContentType = WindowsRuntime]
$null = [Windows.Data.Pdf.PdfDocument, Windows.Data.Pdf, ContentType = WindowsRuntime]
$null = [Windows.Media.Ocr.OcrEngine, Windows.Foundation, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.BitmapDecoder, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Graphics.Imaging.SoftwareBitmap, Windows.Graphics.Imaging, ContentType = WindowsRuntime]
$null = [Windows.Storage.Streams.InMemoryRandomAccessStream, Windows.Storage.Streams, ContentType = WindowsRuntime]
$null = [Windows.Foundation.IAsyncAction, Windows.Foundation, ContentType = WindowsRuntime]

# WinRT async operations surface in PowerShell as IAsyncOperation<T>; bridge them to .NET Tasks.
$asTaskOp = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
        $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0]
$asTaskAction = ([System.WindowsRuntimeSystemExtensions].GetMethods() | Where-Object {
        $_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and
        $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncAction' })[0]
function Await($op, $type) {
    $t = $asTaskOp.MakeGenericMethod($type).Invoke($null, @($op))
    $t.Wait(-1) | Out-Null
    return $t.Result
}
function AwaitAction($act) {
    $t = $asTaskAction.Invoke($null, @($act))
    $t.Wait(-1) | Out-Null
}

$full = (Resolve-Path $PdfPath).Path
$file = Await ([Windows.Storage.StorageFile]::GetFileFromPathAsync($full)) ([Windows.Storage.StorageFile])
$doc = Await ([Windows.Data.Pdf.PdfDocument]::LoadFromFileAsync($file)) ([Windows.Data.Pdf.PdfDocument])
$engine = [Windows.Media.Ocr.OcrEngine]::TryCreateFromUserProfileLanguages()
if ($null -eq $engine) { throw "No Windows OCR engine is available for the user profile languages" }

$sb = New-Object System.Text.StringBuilder
for ($i = 0; $i -lt $doc.PageCount; $i++) {
    $page = $doc.GetPage($i)
    $stream = New-Object Windows.Storage.Streams.InMemoryRandomAccessStream
    $opts = New-Object Windows.Data.Pdf.PdfPageRenderOptions
    $opts.DestinationWidth = [uint32]$Width
    AwaitAction ($page.RenderToStreamAsync($stream, $opts))
    $decoder = Await ([Windows.Graphics.Imaging.BitmapDecoder]::CreateAsync($stream)) ([Windows.Graphics.Imaging.BitmapDecoder])
    $bmp = Await ($decoder.GetSoftwareBitmapAsync()) ([Windows.Graphics.Imaging.SoftwareBitmap])
    $res = Await ($engine.RecognizeAsync($bmp)) ([Windows.Media.Ocr.OcrResult])
    [void]$sb.AppendLine("===== page $($i + 1) / $($doc.PageCount) =====")
    foreach ($ln in $res.Lines) { [void]$sb.AppendLine($ln.Text) }
    $page.Dispose()
    $stream.Dispose()
}
$dir = Split-Path -Parent $OutPath
if ($dir -and -not (Test-Path $dir)) { New-Item -ItemType Directory -Force $dir | Out-Null }
[System.IO.File]::WriteAllText($OutPath, $sb.ToString(), (New-Object System.Text.UTF8Encoding($false)))
Write-Output "ocr $($doc.PageCount) pages -> $OutPath"
