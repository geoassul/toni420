package ....
import java.util.List;

/* Esta clase DB, simulará ser una base de datos para nuestro proyecto*/

public class DB {
	/*todos los objetos podran acceder al mismo dato(Static)
	Esta lista no cambiara cada que se instancie sobre un nuevo objeto
	Sino que todos los objetos estaran referidas a la misma direccion de memoria
	para eso sirve el metodo static simulando una base de datos.
	*el tipo de dato que almacenará el BD serán de tipo Empresa
	private static List<Empresa> listaEmpresas = new ArrayList<>();
	*al usar static estamos diciendo que esta lista será de la clase y no de los objetos
	por lo que podemos simular una persistencia, como si fuese una base de datos.*/
	
	private static Integer llaveSecuencial = 1;
	
	static {
		 
		/*lo que es hace es que cuando se inicialize este objeto DB, se añadiran por defecto
		en la ubicacion de memoria de este objeto con lo que se introduzca dentro del scope.*/
		
		Empresa empresa = new Empresa();
		emoresa.setId(DB.llaveSecuencial++);
		empresa.setNombre("alura");
		Empresa empresa2 = new Empresa();
		empresa2.setId(DB.llaveSecuencial++);
		empresa2.setNombre("alura");
		Empresa empresa3 = new Empresa();
		empresa3.setId(DB.llaveSecuencial++);
		empresa3.setNombre("alura");
		
		listaEmpresas.add(empresa);
		listaEmpresas.add(empresa2);
		listaEmpresas.add(empresa3);
		
		}
	
	
	//metodo para simular una base datos que almacena nombre de empresas
	public void agregarEmpresa(Empresa empresa){
		DB.listaEmpresas.add(empresa); //al agregar DB. estamos especificando que se trata de un objeto de DB
		}
	
	//con este metodo podremos ver la lista de empresas almacenadas en la variable static
	public List<Empresa> getEmpresas(){
		return DB.listaEmpresas;
		}
		
	public void eliminarEmpresa(Integer id) {
		
		Iterator<Empresa> it = listaEmpresas.iterator();
		
		while(it.hasNext()){
			Empresa emp = it.next();
			if(emp.getId() == id){
				it.remove();
				}
			}
		}
		
	public Empresa buscarEmpresaPorId(Integer id){
		
		for (Empresa empresa : listEmpresas){
			if(empresa.getId() == id ){
				return empresa;
				}
			}
		return null;
		}
		
		
		
	}

























