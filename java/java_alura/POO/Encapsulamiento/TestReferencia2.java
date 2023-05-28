
public class TestReferencia2 {
	
	public static void main (String[] args) {
		
		datosTitular diego = new datosTitular();
		diego.nombre = "Diego";
		diego.documento = "444445";
		diego.telefono = "4440232";
		
		
		Cuenta_clase cuentaDeDiego = new Cuenta_clase();
		cuentaDeDiego.titular = diego;
		
		System.out.println(cuentaDeDiego.titular.nombre);
		
		
		
	}
}

