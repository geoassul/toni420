const textArea = document.querySelector(".textarea");
const mensaje = document.querySelector(".mensaje");

function btnEncriptar() {
	texto = textArea.value;
	textoEncrip = encriptador(texto);
	mensaje.value = textoEncrip;
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
		
	let resultado = lista.toString()
	a = resultado.replaceAll(",","");
	
	return a;
	
}

function btnDesencriptar(){
    const textoEncriptado = desencriptar(textArea.value)
    mensaje.value = textoEncriptado
    textArea.value = "";
    
}


function desencriptar(texto){
	let txt = texto;
	let vocales = ["a","e","i","o","u"];
	let criptos = ["ene","aimas","ai","ober","utaf"];
	let contador = 0;
	let index = 0;
	

	for (let palabra of criptos){
		if (txt.includes(palabra)){
			txt = txt.replaceAll(palabra,vocales[contador])
			}
		contador++;
		}
		
	contador = 0;
	alert(txt);
	return txt;
}

function copiar(){
    mensaje.select();
    navigator.clipboard.writeText(mensaje.value)
    mensaje.value = "";
    alert("Texto Copiado")
}
