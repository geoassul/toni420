
import jakarta.servlet.*; // annotation, http, entre otras librerias.

//usando anotaciones, apartir de tomcat 7 se pueden usar.
/*//a partir de tomcat recientes no es necesario usar anotacion, se puede declarar en web.xml
 * las anotaciones("@") reemplazan el uso del web.xml que es donde se hacen las configuraciones
 * para el servlet.
 * Tambien podemos definir mas de dos URL para el servlet
 * */
@WebServlet (urlPatterns = {"/listaEmpresas", "/empresas"})
public class NuevaEmpresaServlet extends HttpServlet{ //exteds para que una clase utilize HTTP
	
	private static final long serialVersionUID = 1l;
	
	@override //es porque modificaremos el metodo de la clase padre
	//doPost solo permite request post, no get.
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException{ //request y response con sus excepciones
			
			//con http podemos enviar String o HTML
			System.out.println("Nueva empresa registrada");
			
			//el retorno de getParameter es siempre una String, por defecto.
			String nombreEmpresa = request.getParameter("nombre"); // recibimos como parametro llamado nombre usado request
			//creamos un parametro llamado fecha que se usara con 
			// el archivo JSP al que ha sido conectado, este metodo nos devuelve un string
			String paramFechaAbertura = request.getParameter("fecha"); 
			//para poder agregar al objeto empresa necesitamos convertir el dato en un tipo Date
			//creamos un objeto SimpleDateFormat para obtener un objeto del JSP(JSTL:fmt) con un formato de fecha(dd/MM/yyyy)
			
			Date fechaAbertura = null; //inicializamos el dato Date para usarlo en el Try,catch.
			try{ //puede que ingresen un mal formato en el input y eso puede producir un error, necesitamos atraparlo
				SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
				fechaAbertura = sdf.parse(paramFechaAbertura);
			} catch(ParseException e) {
				throw new ServletException(e);//al usar tecnologias servlet, es necesario invocar al padre de los errores
				}
			
																		
			
			//agregamos el nombre de la empresa a la BD, otra manera es crear un constructor de empresa
			//que reciba el nombreEmpresa.
			Empresa empresa = new Empresa();
			empresa.setNombre(nombreEmpresa);
			empresa.setFechaAbertura(fechaAbertura);
			
			//Simulacion de base de datos
			DB baseDeDatos = new DB();
			baseDeDatos.agregarEmpresa(empresa);
			
			//hacemos un redireccinamiento para nuestro servlet "listaEmpresas"
			//en este caso estamos reemplazando en RequestDispatcher
			response.SendRedirect("listaEmpresas");
			
			/*
			//Llama al JSP (Dispatcher)
			// el RequestDispatcher nos devuelve un objeto que obtiene al ingresar un archivo jsp
			//IMPORTANTE: el parametro que estamos pasando es un servlet, es decir estamos llamando a otro servlet
			//si quisiera conectarme con un jsp, tendria que utilizar un terminal:: "/listaEmpresas.jsp" 
			RequestDispatcher rd = request.getRequestDispatcher("/listaEmpresas");
			// el primero argumentos es el alias que necesita el JSP para comunicar los parametros del
			//servlet y el JSP, luego el el valor que va a entregar servlet al JSP 
			request.setAttribute("empresa",empresa.getNombre());
			//envia los response y request al JSP
			rd.forward(request,response);
			*/
			
			PrintWriter out = resp.getWriter() // un output que envia datos html
			out.println("<html><body> Empresa " + nombreEmpresa + " fue registrada!</body></html>"); // otra manera de escribir html con service

			System.out.println("Se ejecutó el servlet"); //verificamos que si se ejecuto la llamada http
		}
	
	}

/* Servlet es un objeto al que podemos acceder a traves de una peticion http
 * por medio de nuestro navegador, y es el TOMCAT que se encarga de la administracion
 * y de los métodos.
 * 
 * TomCat es un SERVER CONTAINER, es el encargado de crear los servlets. 
 * es el intermediario entre el SERVLET y el Navegador.(MiddleWare).
 * 
 * El servlet solo se mantedra "vivo" mientras este "levantado" el servidor(TOMCAT)
 * y el servlet solo es iniciado una sola vez, se puede ejecutar muchas veces, pero su
 * inicializacion es solo una vez y es hecha por el tomcat.
 * 
 * ____
 * 
 * *INVERSION DE CONTROL :La inversión de control significa que no es mi método main el que crea instancias de objetos, 
 * 	Tomcat se encarga de crear las instancias.
 * 	
 * TOMCAT se hace cargo de algunas funciones, automaticamente.
 *	*Seguridad
 * 	*Administracion
 * 	*Caché
 * 	los puede hacer, pero no es su especialidad, una mejor opcion es SPRING. 
 *
 * ¡Tomcat solo creará instancias de servlets según sea necesario! 
 * 	Además, instanciará sólo un servlet de cada uno (singleton).
 * 
 *  ¿Que es Deploy?
 * 	subir el proyecto a un servidor.
 * 	-Deploy WAR -( Web ARchive)
 * 	.war es un archivo, su extension se puede usar en muhcos modelos de servidor
 *  JAR y WAR no son más que archivos ZIP,
 *  sin embargo, un WAR tiene los archivos del mundo web como imágenes, CSS, JS, JSP y HTML.
 * 	<<Desarrollo - Produccion>> como entidades que haran uso del DEPLOY
 * 
 * 	en tomcat . deploy es igual a Webapps.
 * 
 * 	Tenemos que definir el tipo de version de java que usará el TOMCAT
 * 	definir la variable de entorno en "editar las variables de entorno del sistema"
 * */
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 














