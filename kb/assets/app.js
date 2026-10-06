/* PSE Equity Microstructure -- offline knowledge base.
 *
 * A hash-routed single page that runs from file://. Data arrives as globals assigned by
 * classic scripts (window.KB_CHAPTERS now, window.KB_FULLTEXT lazily on first search),
 * because fetch/XHR/ES modules are blocked at an opaque origin.
 *
 * Routes:
 *   #/                       home
 *   #/ch/<slug>[/<anchor>]   chapter; anchor = section id, ref-N (reference) or cite-N-K (citation)
 *   #/sources[/<slug>]       source library
 *   #/search/<query>         full results page
 */
(function () {
  "use strict";

  var KB = window.KB_CHAPTERS;
  var view = document.getElementById("view");
  if (!KB || !KB.chapters) {
    view.innerHTML = '<p class="empty">The chapter data did not load (<code>data/kb-chapters.js</code>). ' +
      "Rebuild with <code>python tools/build_kb.py</code>.</p>";
    return;
  }

  var chapters = KB.chapters;
  var bySlug = {};
  chapters.forEach(function (c, i) { c.index = i; bySlug[c.slug] = c; });
  var docById = {};
  KB.searchDocs.forEach(function (d) { docById[d.id] = d; });

  var side = document.getElementById("side");
  var scrim = document.getElementById("scrim");
  var qInput = document.getElementById("q");
  var spanel = document.getElementById("spanel");
  var sresults = document.getElementById("sresults");
  var sstat = document.getElementById("sstat");

  // ------------------------------------------------------------------ helpers
  var ESC = { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" };
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (ch) { return ESC[ch]; }); }
  function escRe(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"); }
  var MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
  function fmtDate(iso) {
    if (!iso) return "";
    var m = /^(\d{4})-(\d{2})(?:-(\d{2}))?/.exec(iso);
    if (!m) return esc(iso);
    return (m[3] ? +m[3] + " " : "") + MONTHS[+m[2] - 1] + " " + m[1];
  }
  function plural(n, w) { return n + " " + w + (n === 1 ? "" : "s"); }
  function pad2(n) { return n < 10 ? "0" + n : String(n); }
  function store(key, val) {
    try { if (val === undefined) return localStorage.getItem(key); localStorage.setItem(key, val); } catch (e) { /* unavailable */ }
    return null;
  }

  // ------------------------------------------------------------------ theme
  document.getElementById("themeBtn").addEventListener("click", function () {
    var root = document.documentElement;
    var cur = root.getAttribute("data-theme") ||
      (window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
    var next = cur === "dark" ? "light" : "dark";
    root.setAttribute("data-theme", next);
    store("pse-kb-theme", next);
  });

  // ------------------------------------------------------------------ navigation drawer
  function closeNav() { side.classList.remove("open"); if (spanel.hidden) scrim.classList.remove("on"); }
  document.getElementById("navToggle").addEventListener("click", function () {
    var open = !side.classList.contains("open");
    side.classList.toggle("open", open);
    scrim.classList.toggle("on", open);
  });
  scrim.addEventListener("click", function () { closeNav(); closeSearch(); scrim.classList.remove("on"); });

  // ------------------------------------------------------------------ sidebar
  function renderSide(activeSlug) {
    var html = [];
    var lastPart = null;
    chapters.forEach(function (c) {
      if (c.part && c.part !== lastPart) { html.push('<div class="grp">' + esc(c.part) + "</div>"); lastPart = c.part; }
      var on = c.slug === activeSlug;
      html.push('<a class="item' + (on ? " on" : "") + '" href="#/ch/' + c.slug + '"><span class="n">' + pad2(c.number) +
        "</span><span>" + esc(c.title) + "</span></a>");
      if (on && c.sections.length) {
        html.push('<div class="secs">');
        c.sections.forEach(function (s) {
          if (s.level === 2) html.push('<a href="#/ch/' + c.slug + "/" + s.anchor + '">' + esc(s.title) + "</a>");
        });
        html.push("</div>");
      }
    });
    html.push('<div class="grp">Reference</div>');
    html.push('<a class="item' + (activeSlug === ":sources" ? " on" : "") + '" href="#/sources"><span class="n">§</span><span>Source library</span></a>');
    html.push('<a class="item' + (activeSlug === ":home" ? " on" : "") + '" href="#/"><span class="n">⌂</span><span>Contents &amp; conventions</span></a>');
    html.push('<div class="foot">Researched to ' + fmtDate(KB.asOf) + "<br>Built " + esc(KB.builtAt) + "</div>");
    side.innerHTML = html.join("");
  }

  // ------------------------------------------------------------------ views
  function totals() {
    var t = { sections: 0, cites: 0, words: 0, archived: 0 };
    chapters.forEach(function (c) { t.sections += c.sections.length; t.cites += c.references.length; t.words += c.words || 0; });
    KB.sources.forEach(function (s) { if (s.local_path) t.archived++; });
    return t;
  }

  function renderHome() {
    var t = totals();
    var out = [];
    out.push('<div class="hero"><h1>' + esc(KB.title) + "</h1>");
    out.push('<div class="meta">Researched to <b>' + fmtDate(KB.asOf) + "</b> · built " + esc(KB.builtAt) + "</div>");
    out.push('<p class="lead">How equities actually trade on the Philippine Stock Exchange — sessions, order handling, ' +
      "auctions, price controls, post-trade, costs, access constraints and the empirical record — written for designing " +
      "execution and trading strategies. Substantive claims are footnoted to a specific page of a source document, " +
      "and archived copies of the sources ship alongside.</p></div>");
    out.push('<div class="stats">' +
      stat(chapters.length, "chapters") + stat(t.sections, "sections") + stat(t.cites, "citations") +
      stat(KB.sources.length, "sources catalogued") + stat(t.archived, "archived locally") +
      stat(t.words >= 1000 ? Math.round(t.words / 1000) + "k" : t.words, "words") + "</div>");
    var lastPart = null, open = false;
    chapters.forEach(function (c) {
      if (c.part !== lastPart || !open) {
        if (open) out.push("</div>");
        if (c.part) out.push('<div class="part-h">' + esc(c.part) + "</div>");
        out.push('<div class="cards">');
        open = true; lastPart = c.part;
      }
      var v = c.vintage;
      var vint = plural(v.sources, "source") + (v.newest ? " · to " + fmtDate(v.newest) : "") +
        (v.undated ? " · " + v.undated + " undated" : "");
      out.push('<a class="card" href="#/ch/' + c.slug + '"><div class="cn">' + pad2(c.number) + '</div><div class="ct">' +
        esc(c.title) + '</div><div class="cs">' + esc(c.summary) + '</div><div class="cv">' + vint + "</div></a>");
    });
    if (open) out.push("</div>");
    out.push('<div class="howto"><h2>Reading conventions</h2><ul>' +
      "<li>Numbered superscripts are citations. Each resolves to a document and, for PDFs, a <b>physical page</b>; " +
      "the reference list opens the archived copy at that page and links the publisher's original.</li>" +
      "<li>Every chapter states the edition-date span of its sources. A rule is only as current as its source; " +
      "the <b>Reform timeline</b> chapter tracks what changed and what is pending.</li>" +
      "<li><b>Execution implications</b> sections translate rules into design decisions. Callouts marked " +
      "<i>Inference</i> are analysis, not rule text.</li>" +
      "<li>Press <kbd>/</kbd> to search chapters and the full text of the archived sources.</li>" +
      '<li>Synthesis for trading design, not legal, tax or compliance advice. See the <a href="#/sources">source library</a> for provenance.</li>' +
      "</ul></div>");
    view.innerHTML = out.join("");
    document.title = "PSE Equity Microstructure";
    renderSide(":home");
  }
  function stat(v, l) { return '<div class="stat"><div class="v">' + esc(v) + '</div><div class="l">' + esc(l) + "</div></div>"; }

  function pageLabel(p) { return p ? (p.indexOf("-") > 0 ? "pp. " + p.replace("-", "–") : "p. " + p) : ""; }

  function renderRefs(c) {
    if (!c.references.length) return "";
    var items = c.references.map(function (r) {
      var meta = [esc(r.publisher)];
      if (r.page) meta.push(pageLabel(r.page));
      if (r.edition && r.edition !== "n/a") meta.push('<span class="badge ' + esc(r.edition) + '">' + esc(r.edition) + "</span>");
      if (r.amended_through) meta.push("dated " + fmtDate(r.amended_through));
      else if (r.type === "pdf") meta.push('<span class="badge undated">undated</span>');
      var links = [];
      if (r.local_path) {
        links.push('<a href="' + esc(r.local_path) + (r.firstPage ? "#page=" + r.firstPage : "") +
          '" target="_blank" rel="noopener">archived copy' + (r.firstPage ? " (p. " + r.firstPage + ")" : "") + "</a>");
      }
      if (r.canonical_url) links.push('<a href="' + esc(r.canonical_url) + '" target="_blank" rel="noopener noreferrer">publisher ↗</a>');
      links.push('<a href="#/sources/' + esc(r.slug) + '">library</a>');
      return '<li id="ref-' + r.n + '"><span class="rn">' + r.n + '</span><div><div class="rt">' + esc(r.title) +
        '</div><div class="rm">' + meta.join(" · ") + '</div><div class="rl">' + links.join("") +
        '<span class="back" data-n="' + r.n + '"></span></div></div></li>';
    });
    return '<section class="refs"><h2 id="refs-list">References</h2><ol>' + items.join("") + "</ol></section>";
  }

  function renderChapter(c) {
    var v = c.vintage;
    var vint = ["<span><b>" + plural(v.sources, "source") + "</b> · " + plural(v.citations, "citation") + "</span>"];
    if (v.oldest) vint.push("<span>source editions <b>" + fmtDate(v.oldest) + "</b> → <b>" + fmtDate(v.newest) + "</b></span>");
    if (v.undated) vint.push('<span class="warn">' + plural(v.undated, "undated source") + "</span>");
    vint.push("<span>researched to <b>" + fmtDate(KB.asOf) + "</b></span>");
    var prev = chapters[c.index - 1], next = chapters[c.index + 1];
    var pager = '<nav class="pager">' +
      (prev ? '<a class="prev" href="#/ch/' + prev.slug + '"><span class="k">← Chapter ' + prev.number + "</span>" + esc(prev.title) + "</a>" : "<span></span>") +
      (next ? '<a class="next" href="#/ch/' + next.slug + '"><span class="k">Chapter ' + next.number + " →</span>" + esc(next.title) + "</a>" : "<span></span>") +
      "</nav>";
    view.innerHTML =
      '<div class="crumb"><a href="#/">Contents</a>' + (c.number ? " · Chapter " + c.number : "") + (c.part ? " · " + esc(c.part) : "") + "</div>" +
      "<h1>" + esc(c.title) + '</h1><p class="lead">' + esc(c.summary) + "</p>" +
      '<div class="vintage">' + vint.join("") + "</div>" +
      '<article class="article">' + c.html + "</article>" + renderRefs(c) + pager;

    // Deep-link affordance on headings.
    view.querySelectorAll(".article h2[id], .article h3[id]").forEach(function (h) {
      var a = document.createElement("a");
      a.className = "hlink"; a.href = "#/ch/" + c.slug + "/" + h.id; a.textContent = "#";
      a.setAttribute("aria-label", "Link to this section");
      h.appendChild(a);
    });
    // Number each occurrence of a citation, and give each reference back-links to them.
    var seen = {};
    view.querySelectorAll(".article sup.cite a").forEach(function (a) {
      var n = a.getAttribute("data-cite");
      seen[n] = (seen[n] || 0) + 1;
      a.parentNode.id = "cite-" + n + "-" + seen[n];
    });
    view.querySelectorAll(".refs .back").forEach(function (b) {
      var n = b.getAttribute("data-n"), k = seen[n] || 0, html = [];
      for (var i = 1; i <= k; i++) html.push('<a href="#/ch/' + c.slug + "/cite-" + n + "-" + i + '">↩' + (k > 1 ? String.fromCharCode(96 + Math.min(i, 26)) : "") + "</a>");
      b.innerHTML = html.join("");
    });
    document.title = c.title + " · PSE Equity Microstructure";
    renderSide(c.slug);
  }

  function renderSources() {
    var groups = {}, order = [];
    KB.sources.forEach(function (s) {
      if (!groups[s.publisher]) { groups[s.publisher] = []; order.push(s.publisher); }
      groups[s.publisher].push(s);
    });
    var out = ['<div class="crumb"><a href="#/">Contents</a> · Reference</div><h1>Source library</h1>',
      '<p class="lead">' + plural(KB.sources.length, "catalogued source") + ", " +
      KB.sources.filter(function (s) { return s.local_path; }).length + " archived in <code>kb/pdfs/</code>. " +
      "Edition status is read from each document's own cover or amendment history, not from its filename.</p>",
      '<input class="filter" id="srcFilter" type="search" placeholder="Filter by title, publisher, slug or note…" aria-label="Filter sources">'];
    order.forEach(function (pub) {
      out.push('<div class="srcgrp"><h2>' + esc(pub) + "</h2>");
      groups[pub].forEach(function (s) {
        var meta = ['<span class="badge">' + esc(s.type) + "</span>"];
        if (s.edition && s.edition !== "n/a") meta.push('<span class="badge ' + esc(s.edition) + '">' + esc(s.edition) + "</span>");
        if (s.amended_through) meta.push("dated " + fmtDate(s.amended_through));
        else if (s.type === "pdf") meta.push('<span class="badge undated">undated</span>');
        if (s.pages) meta.push(plural(s.pages, "page"));
        if (s.citedIn && s.citedIn.length) {
          meta.push("cited in " + s.citedIn.map(function (n) {
            var c = chapters.filter(function (x) { return x.number === n; })[0];
            return c ? '<a href="#/ch/' + c.slug + '">ch. ' + n + "</a>" : "ch. " + n;
          }).join(", "));
        } else meta.push("not cited");
        var links = [];
        if (s.local_path) links.push('<a href="' + esc(s.local_path) + '" target="_blank" rel="noopener">archived copy</a>');
        if (s.canonical_url) links.push('<a href="' + esc(s.canonical_url) + '" target="_blank" rel="noopener noreferrer">publisher ↗</a>');
        out.push('<div class="src" id="src-' + esc(s.slug) + '" data-hay="' +
          esc((s.title + " " + s.publisher + " " + s.slug + " " + (s.note || "")).toLowerCase()) + '">' +
          '<div class="st">' + esc(s.title) + "</div>" +
          '<div class="sm">' + meta.join(" · ") + "</div>" +
          (s.note ? '<div class="sn">' + esc(s.note) + "</div>" : "") +
          '<div class="sl">' + links.join("") + ' <span class="hash">' + esc(s.slug) +
          (s.sha256 ? " · sha256 " + esc(s.sha256.slice(0, 12)) + "…" : "") + "</span></div></div>");
      });
      out.push("</div>");
    });
    view.innerHTML = out.join("");
    var f = document.getElementById("srcFilter");
    f.addEventListener("input", function () {
      var q = f.value.trim().toLowerCase();
      view.querySelectorAll(".src").forEach(function (el) { el.style.display = !q || el.getAttribute("data-hay").indexOf(q) >= 0 ? "" : "none"; });
      view.querySelectorAll(".srcgrp").forEach(function (g) {
        var any = Array.prototype.some.call(g.querySelectorAll(".src"), function (el) { return el.style.display !== "none"; });
        g.style.display = any ? "" : "none";
      });
    });
    document.title = "Source library · PSE Equity Microstructure";
    renderSide(":sources");
  }

  function renderNotFound() {
    view.innerHTML = '<h1>Not found</h1><p class="lead">No page at <code>' + esc(location.hash) + '</code>.</p><p><a href="#/">Back to contents</a></p>';
    renderSide(null);
  }

  // ------------------------------------------------------------------ search
  var msOpts = {
    idField: "id",
    fields: ["title", "text"],
    storeFields: [],
    searchOptions: { boost: { title: 2.5 }, prefix: true, fuzzy: 0.15 }
  };
  var ms = null;
  try {
    ms = new MiniSearch(msOpts);
    ms.addAll(KB.searchDocs);
  } catch (e) {
    ms = null;
    if (window.console) console.error("search index failed to build", e);
  }

  var ft = { state: "idle", ms: null, byId: {} };   // full text of the archived sources
  function loadFulltext() {
    if (ft.state !== "idle") return;
    ft.state = "loading";
    var s = document.createElement("script");
    s.src = "data/kb-fulltext.js";
    s.onload = function () {
      var docs = window.KB_FULLTEXT || [];
      docs.forEach(function (d) { ft.byId[d.id] = d; });
      try {
        ft.ms = new MiniSearch({ idField: "id", fields: ["text"], storeFields: [], searchOptions: { prefix: true, fuzzy: 0.1 } });
        ft.ms.addAllAsync(docs, { chunkSize: 400 }).then(function () {
          ft.state = "ready";
          document.body.setAttribute("data-ft", "ready");
          refreshSearch();
        });
      } catch (e) { ft.state = "failed"; refreshSearch(); }
    };
    s.onerror = function () { ft.state = "failed"; refreshSearch(); };
    document.body.appendChild(s);
  }

  function query(index, q, limit) {
    if (!index || !q) return [];
    var r = index.search(q, { combineWith: "AND" });
    if (!r.length) r = index.search(q, { combineWith: "OR" });
    return r.slice(0, limit);
  }

  function terms(q, hit) {
    var t = q.toLowerCase().split(/[\s,.;:()]+/).filter(function (x) { return x.length > 1; });
    (hit.terms || []).forEach(function (x) { if (t.indexOf(x) < 0) t.push(x); });
    return t.sort(function (a, b) { return b.length - a.length; });
  }

  function highlight(s, ts) {
    if (!ts.length) return esc(s);
    var re = new RegExp(ts.map(escRe).join("|"), "gi"), out = "", last = 0, m;
    while ((m = re.exec(s))) {
      if (!m[0]) { re.lastIndex++; continue; }
      out += esc(s.slice(last, m.index)) + "<mark>" + esc(m[0]) + "</mark>";
      last = m.index + m[0].length;
    }
    return out + esc(s.slice(last));
  }

  function snippet(text, ts, len) {
    len = len || 230;
    var lower = text.toLowerCase(), pos = -1;
    ts.forEach(function (t) { var p = lower.indexOf(t); if (p >= 0 && (pos < 0 || p < pos)) pos = p; });
    var start = pos > 80 ? pos - 80 : 0;
    var s = text.substr(start, len);
    return (start > 0 ? "…" : "") + highlight(s, ts) + (start + len < text.length ? "…" : "");
  }

  function results(q, nCh, nFt) {
    var ch = query(ms, q, nCh).map(function (h) {
      var d = docById[h.id];
      return {
        href: "#/ch/" + d.chapterSlug + (d.anchor ? "/" + d.anchor : ""),
        kind: "Chapter " + d.chapter + " · " + d.chapterTitle,
        title: d.title, snip: snippet(d.text, terms(q, h)), ext: false
      };
    });
    var src = (ft.state === "ready" ? query(ft.ms, q, nFt) : []).map(function (h) {
      var d = ft.byId[h.id];
      return {
        href: (d.path || "#/sources/" + d.slug) + (d.path ? "#page=" + d.page : ""),
        kind: d.publisher + " · p. " + d.page,
        title: d.title, snip: snippet(d.text, terms(q, h)), ext: !!d.path
      };
    });
    return { ch: ch, src: src };
  }

  function resultHtml(r, i) {
    return '<a class="sres" data-i="' + i + '" href="' + esc(r.href) + '"' + (r.ext ? ' target="_blank" rel="noopener"' : "") +
      '><div class="sk">' + esc(r.kind) + '</div><div class="stt">' + esc(r.title) + '</div><div class="ssn">' + r.snip + "</div></a>";
  }

  var sel = -1;
  function runSearch() {
    var q = qInput.value.trim();
    if (!q) { sresults.innerHTML = ""; sstat.textContent = "Type to search"; sel = -1; return; }
    var res = results(q, 10, 8), html = [], i = 0;
    if (res.ch.length) {
      html.push('<div class="sgroup">Chapters</div>');
      res.ch.forEach(function (r) { html.push(resultHtml(r, i++)); });
    }
    if (ft.state === "ready" && res.src.length) {
      html.push('<div class="sgroup">Source documents</div>');
      res.src.forEach(function (r) { html.push(resultHtml(r, i++)); });
    }
    if (!i) html.push('<div class="empty">No matches.</div>');
    html.push('<a class="sres" data-i="' + i + '" href="#/search/' + encodeURIComponent(q) + '"><div class="stt">See all results for “' + esc(q) + "”</div></a>");
    sresults.innerHTML = html.join("");
    sstat.textContent = res.ch.length + " in chapters" +
      (ft.state === "ready" ? " · " + res.src.length + " in sources" : ft.state === "loading" ? " · loading source text…" : ft.state === "failed" ? " · source text unavailable" : "");
    sel = -1;
  }
  function refreshSearch() {
    if (!spanel.hidden) runSearch();
    var r = parseHash();
    if (r.name === "search") renderSearchPage(r.q);
  }

  var timer = null;
  qInput.addEventListener("focus", function () { loadFulltext(); openSearch(); });
  qInput.addEventListener("input", function () {
    openSearch();
    clearTimeout(timer);
    timer = setTimeout(runSearch, 70);
  });
  qInput.addEventListener("keydown", function (e) {
    var items = sresults.querySelectorAll(".sres");
    if (e.key === "ArrowDown" || e.key === "ArrowUp") {
      e.preventDefault();
      if (!items.length) return;
      sel = e.key === "ArrowDown" ? Math.min(items.length - 1, sel + 1) : Math.max(0, sel - 1);
      items.forEach(function (el, i) { el.classList.toggle("on", i === sel); });
      items[sel].scrollIntoView({ block: "nearest" });
    } else if (e.key === "Enter") {
      e.preventDefault();
      var target = items[sel >= 0 ? sel : 0];
      if (target) target.click();
      else if (qInput.value.trim()) location.hash = "#/search/" + encodeURIComponent(qInput.value.trim());
    } else if (e.key === "Escape") {
      closeSearch(); qInput.blur();
    }
  });
  sresults.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a.sres");
    if (a && a.getAttribute("target") !== "_blank") closeSearch();
  });
  function openSearch() { spanel.hidden = false; scrim.classList.add("on"); }
  function closeSearch() { spanel.hidden = true; if (!side.classList.contains("open")) scrim.classList.remove("on"); }
  document.addEventListener("keydown", function (e) {
    var tag = (e.target && e.target.tagName) || "";
    if (e.key === "/" && !/INPUT|TEXTAREA|SELECT/.test(tag)) { e.preventDefault(); qInput.focus(); qInput.select(); }
    else if (e.key === "Escape") { closeSearch(); closeNav(); }
  });

  function renderSearchPage(q) {
    loadFulltext();
    var res = results(q, 60, 60), html = [];
    html.push('<div class="crumb"><a href="#/">Contents</a> · Search</div><h1>Results for “' + esc(q) + "”</h1>");
    html.push('<div class="results">');
    html.push('<h2 class="part-h">Chapters (' + res.ch.length + ")</h2>");
    res.ch.forEach(function (r, i) { html.push(resultHtml(r, i)); });
    if (!res.ch.length) html.push('<div class="empty">No chapter matches.</div>');
    html.push('<h2 class="part-h">Source documents' + (ft.state === "ready" ? " (" + res.src.length + ")" : "") + "</h2>");
    if (ft.state === "ready") {
      res.src.forEach(function (r, i) { html.push(resultHtml(r, i)); });
      if (!res.src.length) html.push('<div class="empty">No source-document matches.</div>');
    } else {
      html.push('<div class="empty">' + (ft.state === "failed" ? "Source text unavailable." : "Loading source text…") + "</div>");
    }
    html.push("</div>");
    view.innerHTML = html.join("");
    document.title = "Search: " + q + " · PSE Equity Microstructure";
    renderSide(null);
  }

  // ------------------------------------------------------------------ router
  function parseHash() {
    var h = location.hash.replace(/^#\/?/, "");
    if (!h) return { name: "home", key: "home" };
    var parts = h.split("/");
    if (parts[0] === "ch" && parts[1]) {
      return { name: "chapter", slug: parts[1], anchor: parts[2] ? decodeURIComponent(parts[2]) : "", key: "ch:" + parts[1] };
    }
    if (parts[0] === "sources") {
      return { name: "sources", anchor: parts[1] ? "src-" + decodeURIComponent(parts[1]) : "", key: "sources" };
    }
    if (parts[0] === "search") {
      var q = decodeURIComponent(parts.slice(1).join("/"));
      return { name: "search", q: q, key: "search:" + q };
    }
    return { name: "notfound", key: "nf:" + h };
  }

  function scrollToAnchor(id) {
    var el = document.getElementById(id);
    if (!el) return false;
    el.scrollIntoView({ block: id.indexOf("cite-") === 0 ? "center" : "start" });
    var target = el.tagName === "SUP" ? el.firstChild : el;
    target.classList.remove("flash");
    void target.offsetWidth;  // restart the animation
    target.classList.add("flash");
    return true;
  }

  var currentKey = null;
  function route() {
    var r = parseHash();
    closeSearch();
    closeNav();
    var changed = r.key !== currentKey;
    if (changed) {
      currentKey = r.key;
      if (r.name === "home") renderHome();
      else if (r.name === "chapter") {
        var c = bySlug[r.slug];
        if (c) renderChapter(c); else renderNotFound();
      } else if (r.name === "sources") renderSources();
      else if (r.name === "search") { qInput.value = r.q; renderSearchPage(r.q); }
      else renderNotFound();
    }
    // Same view and no anchor (e.g. browser Back from a reference): leave scroll alone so
    // the reader returns to where they were.
    if (r.anchor) { if (!scrollToAnchor(r.anchor) && changed) window.scrollTo(0, 0); }
    else if (changed) window.scrollTo(0, 0);
  }

  // Clicking a link to the hash we are already on fires no hashchange; scroll anyway.
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest('a[href^="#/"]');
    if (a && a.getAttribute("href") === location.hash) { e.preventDefault(); route(); var r = parseHash(); if (r.anchor) scrollToAnchor(r.anchor); }
  });

  window.addEventListener("hashchange", route);
  route();
  document.body.setAttribute("data-ready", "1");
})();
