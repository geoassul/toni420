
public class SistemaInterno {
	
	private String clave = "AluraCursos";
	
	public boolean autentica(FuncionarioAutenticable gerente) {
		boolean puedeIniciarSesion = gerente.iniciarSesion(clave);
		
		if (puedeIniciarSesion){
			System.out.println("login exitoso");
			return true;
		}
		else{
			System.out.println("clave incorrecta");
			return false;
		}
	}
}

