
public class TestSistemaInterno {
	
	public static void main (String[] args) {
		
		SistemaInterno sistema = new SistemaInterno();
		Autenticable gerente1 = new Gerente();
		Autenticable admin = new Administrador();

		gerente1.setClave("AluraCursos");
		sistema.autentica(gerente1);
		sistema.autentica(admin);
		
		}
	
	}
