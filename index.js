var usuario= "a@gmail.com"
var contrasena="1234"

var userg= document.getElementById("Entrada1").value
var pass= document.getElementById("Entrada2").value  

function enviar(Entrada1, Entrada2) {
    if (Entrada1 === userg && Entrada2 === pass) {
        alert("Bienvenido!");
        
    } else {
        alert("No se pudo iniciar sesión");
    }
}