const textArea = document.querySelector(".textarea");
const mensaje = document.querySelector(".mensaje");

function btnEncriptar() {
	texto = textArea.value;
	textoEncrip = encriptador(texto);
	mensaje.value = textoEncrip;
	//alert(texto);
}


function encriptador(texto) {
	let txt = texto;
	let vocales = ["a","e","i","o","u"];
	let criptos = ["ene","aimas","ai","ober","utaf"];
	let lista = texto.split("");
	let contador = 0;
	let index = 0;
	
	for(let char of txt){
		
		//alert("entro " + txt.length +" "+ char );
		
		for (let vocal of vocales){
			//alert("entro" + vocal);
			if (vocal == char){
				lista[index] = criptos[contador];
				//alert("entro"+lista[index]);
				}
			contador++;
			}
			//alert("contador: " + contador);
		contador = 0;	
		index++
		if (index == txt.length){
			break;
			}
			
		//alert("index: " + index);		
		}
		
	let resultado = lista.toString()
	a = resultado.replaceAll(",","");
	alert(a);
	
	return a;
	
}
