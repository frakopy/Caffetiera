const inputName = document.getElementById("id_name")
const inputEmail = document.getElementById("id_email")
const inputContent = document.getElementById("id_content")

inputName.classList.add('form-control')
inputName.placeholder = 'Escribe tu nombre'

inputEmail.classList.add('form-control')
inputEmail.placeholder = 'Escribe tu emial'

inputContent.classList.add('form-control')
inputContent.placeholder = 'Escribe tu mensaje'
inputContent.rows = 3

