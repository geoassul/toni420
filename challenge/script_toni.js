const textArea = document.querySelector(".textarea");
const mensaje = document.querySelector(".mensaje");
const mensaje_area = document.querySelector(".advertencia_result");
const imagen_result = document.querySelector(".Muñeco");

function btnEncriptar() {
	texto = textArea.value;
	textoEncrip = encriptador(texto);
	mensaje.value = textoEncrip;
	consulta();
}


function encriptador(texto) {
	let txt = texto;
	let vocales = ["a","e","i","o","u"];
	let criptos = ["ene","aimas","ai","ober","utaf"];
	let lista = texto.split("");
	let contador = 0;
	let index = 0;
	
	for(let char of txt){

		for (let vocal of vocales){
			if (vocal == char){
				lista[index] = criptos[contador];
				}
			contador++;
			}
		contador = 0;	
		index++;
				
		}
		
	let resultado = lista.toString();
	a = resultado.replaceAll(",","");
	
	return a;
	
}

function btnDesencriptar(){
    const textoEncriptado = desencriptar(textArea.value);
    mensaje.value = textoEncriptado;
    consulta();
}


function desencriptar(texto){
	let txt = texto;
	let vocales = ["a","e","i","o","u"];
	let criptos = ["ene","aimas","ai","ober","utaf"];
	let contador = 0;
	let index = 0;
	

	for (let palabra of criptos){
		if (txt.includes(palabra)){
			txt = txt.replaceAll(palabra,vocales[contador]);
			}
		contador++;
		}

	contador = 0;
	return txt;
}

function copiar(){
    mensaje.select();
    navigator.clipboard.writeText(mensaje.value);
    mensaje.value = "";
	textArea.value = "";
    consulta();
    alert("Texto Copiado");
}

function consulta(){
	
	if (mensaje.value.length > 0){
		mensaje_area.style.display = "none";
		mensaje.style.background = "#E5E5E5";
		}
	else{
		mensaje_area.style.display = "block";
		mensaje.style.background = "url(imagenes/Muñeco.png) center center no-repeat"
		}
		
	}
