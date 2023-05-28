
public class Gerente extends Funcionario implements Autenticable{
    
    private Autenticacion util;
    
    @Override
    public double getBonificacion() {
        System.out.println("ejecutando desde gerente");
        return 2000;
        //return super.getSalario() + this.getSalario() * 0.5;
    }
    
    @Override
    public void setClave(String clave){
        this.util.setClave(clave);
        }

    @Override
    public boolean iniciarSesion(String clave){
        return this.util.iniciarSesion(clave);
        }

}
