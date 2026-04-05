(function () {
  var form = document.getElementById("properties-filter-form");
  if (!form) return;

  function submitForm() {
    form.submit();
  }

  var citySelect = form.querySelector("select#filter-city");
  var projectTypeSelect = form.querySelector("select#filter-project-type");

  if (citySelect) citySelect.addEventListener("change", submitForm);
  if (projectTypeSelect) projectTypeSelect.addEventListener("change", submitForm);

  form.querySelectorAll('input[name="status"]').forEach(function (cb) {
    cb.addEventListener("change", submitForm);
  });
})();
