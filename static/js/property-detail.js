(function () {
  var main = document.getElementById("pd-gallery-main-img");
  var thumbs = document.querySelectorAll(".pd-gallery-thumb");
  if (!main || !thumbs.length) return;

  var total = thumbs.length;
  var name = main.getAttribute("alt");
  var nameBase = name ? name.replace(/\s*—\s*photo\s+\d+\s+of\s+\d+.*$/i, "").trim() : "";

  thumbs.forEach(function (btn) {
    btn.addEventListener("click", function () {
      var src = btn.getAttribute("data-full-src");
      var idx = btn.getAttribute("data-index");
      if (!src) return;
      main.src = src;
      if (nameBase && idx) {
        main.setAttribute("alt", nameBase + " — photo " + idx + " of " + total);
      }
      thumbs.forEach(function (t) {
        var on = t === btn;
        t.classList.toggle("is-active", on);
        t.setAttribute("aria-selected", on ? "true" : "false");
      });
    });
  });
})();
