

public class Anotaciones {
	
	public class Usuario {

		private String nombre;
		private String identidad;
		private LocalDate fechaNacimiento;
	}
	public boolean usuarioValido(Usuario usuario){
	   if(!usuario.getNombre().matches("[a-zA-Záàâãéèêíïóôõöúçñ\\s]+")){
		  return false;
	   }
	   if(!usuario.getIdentidad().matches("[^0-9]+")){
		  return false;
	   }
	   return Period.between(usuario.getFechaNacimiento(), LocalDate.now()).getYears() >= 18;
	}
	
	public static void main (String[] args) {
		
	}
}

