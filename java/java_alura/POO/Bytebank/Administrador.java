
public class Administrador extends Funcionario implements Autenticable {
	
	private AutenticacionUtil util;
	
	@Override
	public double getBonificacion(){
		return 0;
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

