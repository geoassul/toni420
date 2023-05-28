public class TestReferencia {

    public static void main(String[] args) {

        Cuenta_clase miCuenta = new Cuenta_clase();
        miCuenta.saldo = 500.0;
        Cuenta_clase otraCuenta = miCuenta;
        otraCuenta.saldo += 1000.0;

        System.out.println(miCuenta.saldo);
		System.out.println(otraCuenta);
        System.out.println(miCuenta);

        
    }
}
