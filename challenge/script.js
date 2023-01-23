const textArea = document.querySelector(".textarea");
const mensaje = document.querySelector(".mensaje");

function btnEncriptar() {
	const textoEncriptado = encriptador(textArea.value);
	mensaje.value = textoEncriptado;
}
	
	
function encriptador(texto){
	let matrizCodigo = [["a","ene"],["e","imes"],["i","ai"],["o","ober"],["u","ufat"]];
	texto = texto.toLowerCase();
	
	for (let i = 0; i < matrizCodigo.length; i++){
		if(texto.includes(matrizCodigo[i][0])){
			texto = texto.replaceAll(matrizCodigo[i][0],matrizCodigo[i][1]);
		}
	}
	
	return texto;
}
