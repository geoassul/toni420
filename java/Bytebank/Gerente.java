
public class Gerente extends FuncionarioAutenticable{
    
    @Override
    public double getBonificacion() {
        System.out.println("ejecutando desde gerente");
        return 2000;
        //return super.getSalario() + this.getSalario() * 0.5;
    }

}
