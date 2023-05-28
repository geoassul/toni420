public class Parerga1 {

    public static void main(String[] args) {

        double salario = 3830.0;
        // ifs aqui
        if (salario >= 1900 && salario < 2800){
			double impuesto = 0.075;
			int deduccion = 142;
			salario = (salario - (salario * impuesto)) + deduccion;
			System.out.println(impuesto + " s" + deduccion);
			}
		else if (salario >= 2800.01 && salario < 3751.0){
			double impuesto = 0.15;
			int deduccion = 350;
			salario = (salario - (salario * impuesto)) + deduccion;
			System.out.println(impuesto + " s" + deduccion);
			}
		else if (salario >= 3751.01 && salario < 4664.00){
			double impuesto = 0.225;
			int deduccion = 636;
			salario = (salario - (salario * impuesto)) + deduccion;
			System.out.println(impuesto + " s" + deduccion);
			}
			
		System.out.println(salario);
    }
}
