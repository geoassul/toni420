
/*creamos un objeto que almacenara los datos de una empresa para nuestro proyecto*/
public class Empresa {
	
	private Integer id; //identificador,necesario si usas mapeamiento con JPA 
	private String nombre;
	private Date fechaAbertura = new Date();
	
	//Getters y Setters(id, nombre)
	public void setFechaAbertura(Date fechaAbertura){
		this.fechaAbertura = fechaAbertura;
		}
	public void getFechaAbertura(){
		return fechaAbertura;
	}
	public void setId(Integer id){
		this.id = id;
		}
	public Integer getId(){
		return id;
		}
	public void setNombre(String nombre){
		this.nombre = nombre;
		}
	public String getNombre(){
		return nombre;
		}
	
	}




















