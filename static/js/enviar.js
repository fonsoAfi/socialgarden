// function actualizarContenido() {
//     fetch('=URL(register)')  // Cambia la URL por la ruta de tu backend
//         .then(response => {
//             if (!response.ok) throw new Error('Error en la respuesta del servidor');
//             return response.text();
//         })
//         .then(data => {
//             // Actualiza el contenido de la sección
//             document.getElementById('form-registro').innerHTML = data;
//         })
//         .catch(error => {
//             console.error('Error al obtener los datos:', error);
//             window.location.reload()
//         });
// }

const email = document.getElementById("email");

document.addEventListener("submit", function (event) {
  if (email.validity.valid) {
    emailError.innerHTML = ""; // Restablece el contenido del mensaje
    emailError.className = "error"; // Restablece el estado visual del mensaje
  } else {
    event.preventDefault()
    showError()
  }
});


function showError() {
    if (email.validity.valueMissing) {
        // Si el campo está vacío
        // muestra el mensaje de error siguiente.
        emailError.textContent =
          "Debe introducir una dirección de correo electrónico.";
      } else if (email.validity.typeMismatch) {
        // Si el campo no contiene una dirección de correo electrónico
        // muestra el mensaje de error siguiente.
        emailError.textContent =
          "El valor introducido debe ser una dirección de correo electrónico.";
      } else if (email.validity.tooShort) {
        // Si los datos son demasiado cortos
        // muestra el mensaje de error siguiente.
        emailError.textContent =
          "El correo electrónico debe tener al menos ${ email.minLength } caracteres; ha introducido ${ email.value.length }."
      }
}