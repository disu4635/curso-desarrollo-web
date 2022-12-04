function validateForm(data) {
  const errors = {};
  let hasErrors = false;
  if (data.name === "") {
    errors.name = "El nombre es requerido";
    hasErrors = true;
  }
  if (data.age === "") {
    errors.age = "La edad es requerida";
    hasErrors = true;
  } else if (isNaN(data.age)) {
    errors.age = "La edad no es un número";
    hasErrors = true;
  } else if (data.age < 18) {
    errors.age = "No es mayor de edad";
    hasErrors = true;
  }
  if (data.profession === "") {
    errors.profession = "La profesión es requerida";
    hasErrors = true;
  }
  return hasErrors ? errors : null;
}

const $form = document.getElementById("form");
const $name = document.getElementById("name");
const $age = document.getElementById("age");
const $profession = document.getElementById("profession");

$form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = {
    name: $name.value.trim(),
    age: $age.value.trim(),
    profession: $profession.value.trim(),
  };
  const errors = validateForm(data);
  if (errors === null) {
    alert("Datos validos");
  } else {
    alert(`${["Datos invalidos:", ...Object.values(errors)].join("\n - ")}`);
  }
});
