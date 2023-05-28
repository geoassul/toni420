
public class PruebaAcceso {
	
	public static void main (String[] args) {
		Cuenta_clase cuenta = new Cuenta_clase();
		cuenta.deposito(300);
		System.out.println(cuenta.obtenerSaldo());
	}
}

