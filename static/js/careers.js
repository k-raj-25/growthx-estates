(function () {
  const main = document.querySelector(".careers-page");
  const dataEl = document.getElementById("careers-openings-data");
  const listEl = document.getElementById("careers-openings-list");
  const modal = document.getElementById("careers-job-modal");
  const deptFilter = document.getElementById("careers-department-filter");
  const countEl = document.getElementById("careers-openings-count");
  const filterEmptyEl = document.getElementById("careers-openings-filter-empty");

  if (!main || !dataEl || !listEl || !modal) return;

  let openings;
  try {
    openings = JSON.parse(dataEl.textContent);
  } catch {
    return;
  }

  const byId = Object.fromEntries(openings.map((o) => [String(o.id), o]));
  const hrEmail = main.dataset.hrEmail || "";

  const titleEl = modal.querySelector("#careers-job-modal-title");
  const metaEl = modal.querySelector("#careers-job-modal-meta");
  const overviewEl = modal.querySelector("#careers-job-modal-overview");
  const respEl = modal.querySelector("#careers-job-modal-responsibilities");
  const qualEl = modal.querySelector("#careers-job-modal-qualifications");
  const applyEl = modal.querySelector("#careers-job-modal-apply");
  const hrLinkEl = modal.querySelector("#careers-job-modal-hr-link");

  let openTrigger = null;

  function renderMetaChips(container, opening) {
    container.replaceChildren();
    const rows = [];
    if (opening.department) rows.push(["Team", opening.department]);
    if (opening.location) rows.push(["Location", opening.location]);
    if (opening.employmentType) rows.push(["Type", opening.employmentType]);
    rows.forEach(([label, value]) => {
      const chip = document.createElement("span");
      chip.className = "careers-job-meta-chip";
      const lb = document.createElement("span");
      lb.className = "careers-job-meta-chip-label";
      lb.textContent = label;
      const val = document.createElement("span");
      val.className = "careers-job-meta-chip-value";
      val.textContent = value;
      chip.append(lb, val);
      container.appendChild(chip);
    });
  }

  function formatBulletBlock(text, container) {
    container.textContent = "";
    const lines = (text || "")
      .split("\n")
      .map((l) => l.trim())
      .filter(Boolean);
    if (!lines.length) {
      const p = document.createElement("p");
      p.className = "careers-modal-empty";
      p.textContent = "Details will be posted soon. You can still apply with a note on your fit for the role.";
      container.appendChild(p);
      return;
    }
    const ul = document.createElement("ul");
    ul.className = "careers-modal-list";
    lines.forEach((line) => {
      const li = document.createElement("li");
      li.textContent = line.replace(/^[-•]\s*/, "");
      ul.appendChild(li);
    });
    container.appendChild(ul);
  }

  function setOverview(text) {
    overviewEl.textContent = "";
    const p = document.createElement("p");
    p.className = "careers-modal-overview-text";
    p.textContent = (text || "").trim() || "No overview provided yet.";
    overviewEl.appendChild(p);
  }

  function openModal(opening) {
    if (!opening) return;
    openTrigger = document.activeElement;
    titleEl.textContent = opening.title;
    renderMetaChips(metaEl, opening);

    setOverview(opening.description);
    formatBulletBlock(opening.responsibilities, respEl);
    formatBulletBlock(opening.qualifications, qualEl);

    const subj = `Application: ${opening.title}`;
    applyEl.href = `mailto:${hrEmail}?subject=${encodeURIComponent(subj)}`;
    applyEl.textContent = "Apply by email";
    if (hrLinkEl) {
      hrLinkEl.textContent = hrEmail;
      hrLinkEl.href = `mailto:${hrEmail}?subject=${encodeURIComponent(subj)}`;
    }

    modal.hidden = false;
    modal.setAttribute("aria-hidden", "false");
    document.documentElement.style.overflow = "hidden";
    document.body.classList.add("careers-job-modal-open");

    document.querySelectorAll(".js-careers-opening-open").forEach((btn) => {
      btn.setAttribute("aria-expanded", "false");
    });
    const activeBtn = listEl.querySelector(
      `.js-careers-opening-open[data-opening-id="${opening.id}"]`
    );
    if (activeBtn) activeBtn.setAttribute("aria-expanded", "true");

    modal.querySelector(".js-careers-job-modal-close")?.focus();
  }

  function closeModal() {
    modal.hidden = true;
    modal.setAttribute("aria-hidden", "true");
    document.documentElement.style.overflow = "";
    document.body.classList.remove("careers-job-modal-open");
    document.querySelectorAll(".js-careers-opening-open").forEach((btn) => {
      btn.setAttribute("aria-expanded", "false");
    });
    if (openTrigger && typeof openTrigger.focus === "function") {
      openTrigger.focus();
    }
    openTrigger = null;
  }

  function visibleItems() {
    return [...listEl.querySelectorAll(".careers-opening-item")].filter(
      (li) => !li.hidden
    );
  }

  function updateFilterUI() {
    const vis = visibleItems();
    const total = listEl.querySelectorAll(".careers-opening-item").length;
    if (countEl) {
      if (deptFilter && deptFilter.value) {
        countEl.textContent =
          vis.length === 0
            ? "No roles in this department"
            : `Showing ${vis.length} of ${total} role${total === 1 ? "" : "s"}`;
      } else {
        countEl.textContent = `${total} open role${total === 1 ? "" : "s"}`;
      }
    }
    if (filterEmptyEl) {
      const empty = deptFilter && deptFilter.value && vis.length === 0;
      filterEmptyEl.hidden = !empty;
    }
  }

  function applyDepartmentFilter() {
    const val = deptFilter ? deptFilter.value : "";
    listEl.querySelectorAll(".careers-opening-item").forEach((li) => {
      const d = li.getAttribute("data-department") || "";
      if (!val || d === val) {
        li.hidden = false;
      } else {
        li.hidden = true;
      }
    });
    updateFilterUI();
  }

  listEl.addEventListener("click", (e) => {
    const btn = e.target.closest(".js-careers-opening-open");
    if (!btn) return;
    const id = btn.getAttribute("data-opening-id");
    const opening = byId[id];
    if (opening) openModal(opening);
  });

  deptFilter?.addEventListener("change", applyDepartmentFilter);

  modal.querySelectorAll(".js-careers-job-modal-dismiss").forEach((el) => {
    el.addEventListener("click", closeModal);
  });
  modal.querySelectorAll(".js-careers-job-modal-close").forEach((el) => {
    el.addEventListener("click", closeModal);
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && !modal.hidden) {
      closeModal();
    }
  });

  applyDepartmentFilter();
})();
