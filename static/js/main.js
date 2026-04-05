(function () {
  const header = document.querySelector(".header");
  const menuToggle = document.querySelector(".menu-toggle");
  const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  if (menuToggle && header) {
    const backdrop = header.querySelector(".nav-backdrop");
    const drawer = header.querySelector(".nav-drawer");
    const navDropdowns = header.querySelectorAll(".nav-dropdown");
    const navDrawerMq = window.matchMedia("(max-width: 900px)");

    function closeAllNavDropdowns() {
      navDropdowns.forEach((dd) => {
        dd.classList.remove("is-open");
        dd.querySelector(".nav-dropdown-toggle")?.setAttribute("aria-expanded", "false");
      });
    }

    function setNavOpen(open) {
      header.classList.toggle("nav-open", open);
      menuToggle.setAttribute("aria-expanded", open ? "true" : "false");
      menuToggle.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      if (!open) closeAllNavDropdowns();
    }

    menuToggle.addEventListener("click", () => {
      setNavOpen(!header.classList.contains("nav-open"));
    });

    backdrop?.addEventListener("click", () => setNavOpen(false));

    document.querySelectorAll(".nav a").forEach((link) => {
      link.addEventListener("click", () => setNavOpen(false));
    });

    navDropdowns.forEach((dd) => {
      const btn = dd.querySelector(".nav-dropdown-toggle");
      if (!btn) return;
      btn.addEventListener("click", () => {
        if (!navDrawerMq.matches) return;
        const next = !dd.classList.contains("is-open");
        navDropdowns.forEach((other) => {
          if (other !== dd) {
            other.classList.remove("is-open");
            other.querySelector(".nav-dropdown-toggle")?.setAttribute("aria-expanded", "false");
          }
        });
        dd.classList.toggle("is-open", next);
        btn.setAttribute("aria-expanded", next ? "true" : "false");
      });
    });
    navDrawerMq.addEventListener("change", () => {
      if (!navDrawerMq.matches) closeAllNavDropdowns();
    });

    drawer?.querySelector(".btn-nav")?.addEventListener("click", () => setNavOpen(false));

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && header.classList.contains("nav-open")) {
        setNavOpen(false);
      }
    });
  }

  function easeOutQuart(t) {
    return 1 - Math.pow(1 - t, 4);
  }

  function formatCount(value, useComma) {
    if (useComma) return value.toLocaleString("en-US");
    return String(value);
  }

  function animateCount(el) {
    if (el.dataset.counted === "1") return;
    el.dataset.counted = "1";

    const target = parseInt(el.getAttribute("data-target"), 10);
    const suffix = el.getAttribute("data-suffix") || "";
    const useComma = target >= 1000;
    const duration = reducedMotion ? 0 : 2100;
    const start = performance.now();

    if (duration === 0) {
      el.textContent = formatCount(target, useComma) + suffix;
      return;
    }

    function frame(now) {
      const elapsed = now - start;
      const t = Math.min(elapsed / duration, 1);
      const eased = easeOutQuart(t);
      const value = Math.round(eased * target);
      el.textContent = formatCount(value, useComma) + suffix;
      if (t < 1) requestAnimationFrame(frame);
    }

    requestAnimationFrame(frame);
  }

  function initCounters() {
    document.querySelectorAll(".js-count").forEach(animateCount);
  }

  const statsBlock = document.querySelector(".hero-stats");
  if (statsBlock && !reducedMotion) {
    const counterObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            window.setTimeout(initCounters, 520);
            counterObserver.disconnect();
          }
        });
      },
      { threshold: 0.25, rootMargin: "0px" }
    );
    counterObserver.observe(statsBlock);
  } else if (statsBlock) {
    initCounters();
  }

  const revealEls = document.querySelectorAll(".reveal");
  if (revealEls.length && !reducedMotion) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.08, rootMargin: "0px 0px -40px 0px" }
    );
    revealEls.forEach((el) => revealObserver.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add("is-visible"));
  }

  const awardLightbox = document.querySelector("#award-lightbox");
  if (awardLightbox) {
    const lightboxImg = awardLightbox.querySelector(".award-lightbox-img");

    function openAwardLightbox(src, alt) {
      if (!lightboxImg || !src) return;
      lightboxImg.src = src;
      lightboxImg.alt = alt || "";
      awardLightbox.hidden = false;
      awardLightbox.setAttribute("aria-hidden", "false");
      document.body.classList.add("award-lightbox-open");
      document.documentElement.style.overflow = "hidden";
    }

    function closeAwardLightbox() {
      awardLightbox.hidden = true;
      awardLightbox.setAttribute("aria-hidden", "true");
      document.body.classList.remove("award-lightbox-open");
      document.documentElement.style.overflow = "";
      if (lightboxImg) {
        lightboxImg.removeAttribute("src");
        lightboxImg.alt = "";
      }
    }

    document.addEventListener("click", (e) => {
      const btn = e.target.closest(".js-award-lightbox-open");
      if (!btn) return;
      const src = btn.getAttribute("data-lightbox-src") || "";
      const alt = btn.getAttribute("data-lightbox-alt") || "";
      openAwardLightbox(src, alt);
    });

    awardLightbox.querySelector(".js-award-lightbox-dismiss")?.addEventListener("click", closeAwardLightbox);
    awardLightbox.querySelector(".js-award-lightbox-close")?.addEventListener("click", closeAwardLightbox);

    document.addEventListener("keydown", (e) => {
      if (e.key === "Escape" && !awardLightbox.hidden) {
        closeAwardLightbox();
      }
    });
  }
})();
