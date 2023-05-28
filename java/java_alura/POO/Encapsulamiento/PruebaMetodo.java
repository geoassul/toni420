
public class PruebaMetodo {
	
	public static void main (String[] args) {
		Cuenta_clase miCuenta = new Cuenta_clase();
		miCuenta.saldo = 2000;
		//System.out.println("tu saldo es: " );
		miCuenta.deposito(200.50);
		miCuenta.retirar(1000.0);
		Cuenta_clase cuenta2 = new Cuenta_clase();
		cuenta2.deposito(18000);
		cuenta2.transferir(500,miCuenta);
		
		}
}

