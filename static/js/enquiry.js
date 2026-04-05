(function () {
  function getCsrf() {
    var meta = document.querySelector('meta[name="csrf-token"]');
    if (meta) {
      var c = meta.getAttribute("content");
      if (c) return c;
    }
    var inp = document.querySelector("[name=csrfmiddlewaretoken]");
    return inp ? inp.value : "";
  }

  function getSubmitUrl() {
    var b = document.body;
    return b ? b.getAttribute("data-enquiry-submit-url") || "" : "";
  }

  function clearFieldErrors(form) {
    form.querySelectorAll(".enquiry-field-error").forEach(function (el) {
      el.hidden = true;
      el.textContent = "";
    });
  }

  function showErrors(form, errors) {
    if (!errors) return;
    Object.keys(errors).forEach(function (key) {
      var el = form.querySelector('[data-error-for="' + key + '"]');
      if (el && errors[key]) {
        el.textContent = errors[key];
        el.hidden = false;
      }
    });
    var status = form.querySelector("[data-enquiry-status]");
    if (status && errors._error) {
      status.textContent = errors._error;
      status.hidden = false;
      status.classList.add("is-error");
    }
  }

  function setStatus(form, message, isError) {
    var status = form.querySelector("[data-enquiry-status]");
    if (!status) return;
    status.textContent = message || "";
    status.hidden = !message;
    status.classList.toggle("is-error", !!isError);
  }

  function closeCallbackModal(modal) {
    modal.classList.remove("is-open");
    modal.setAttribute("aria-hidden", "true");
    document.documentElement.style.overflow = "";
    var form = modal.querySelector(".js-enquiry-form");
    if (form) {
      clearFieldErrors(form);
      setStatus(form, "", false);
    }
  }

  function openCallbackModal(modal) {
    modal.classList.add("is-open");
    modal.setAttribute("aria-hidden", "false");
    document.documentElement.style.overflow = "hidden";
    var firstInput = modal.querySelector(".enquiry-input");
    if (firstInput) window.setTimeout(function () { firstInput.focus(); }, 10);
  }

  function bindEnquiryForm(form) {
    var url = getSubmitUrl();
    if (!url) return;

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      clearFieldErrors(form);
      setStatus(form, "", false);

      var btn = form.querySelector('button[type="submit"]');
      if (btn) btn.disabled = true;

      fetch(url, {
        method: "POST",
        headers: { "X-CSRFToken": getCsrf() },
        body: new FormData(form),
        credentials: "same-origin",
      })
        .then(function (r) {
          return r.json().then(function (data) {
            return { ok: r.ok, data: data };
          });
        })
        .then(function (res) {
          if (res.ok && res.data && res.data.ok) {
            form.reset();
            setStatus(
              form,
              "Thank you — we will get back to you shortly.",
              false
            );
            var modal = form.closest("[data-callback-modal]");
            if (modal) {
              window.setTimeout(function () {
                closeCallbackModal(modal);
              }, 1600);
            }
          } else {
            var err = (res.data && res.data.errors) || {};
            showErrors(form, err);
            if (!Object.keys(err).length) {
              setStatus(form, "Something went wrong. Please try again.", true);
            }
          }
        })
        .catch(function () {
          setStatus(form, "Something went wrong. Please try again.", true);
        })
        .finally(function () {
          if (btn) btn.disabled = false;
        });
    });
  }

  document.querySelectorAll(".js-enquiry-form").forEach(bindEnquiryForm);

  document.querySelectorAll("[data-callback-modal]").forEach(function (modal) {
    modal.querySelectorAll("[data-close-callback-modal]").forEach(function (el) {
      el.addEventListener("click", function () {
        closeCallbackModal(modal);
      });
    });
  });

  document.querySelectorAll("[data-open-callback-modal]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var modal = document.querySelector("[data-callback-modal]");
      if (modal) openCallbackModal(modal);
    });
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    document.querySelectorAll("[data-callback-modal].is-open").forEach(closeCallbackModal);
  });
})();
