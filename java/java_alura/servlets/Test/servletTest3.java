import jakarta.servlet.*; // annotation, http, entre otras librerias.

//usando anotaciones, apartir de tomcat 7 se pueden usar.
//@webServlet(urlPatterns = "/hola") //a partir de tomcat recientes no es necesario usar anotacion, se puede declarar en web.xml
public class ServletTest3 extends HttpServlet{ //exteds para que una clase utilize HTTP
	
	@override //es porque modificaremos el metodo de la clase padre
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException{ //request y response con sus excepciones
			//con http podemos enviar String o HTML
			System.out.println("Nueva empresa registrada");
			String nombreEmpresa = request.getParameter("nombre"); // recibimos como parametro llamado nombre usado request
			PrintWriter out = resp.getWriter() // un output que envia datos html
			out.println("<html><body> Empresa " + nombreEmpresa + " fue registrada!</body></html>"); // otra manera de escribir html con service
			
			System.out.println("Se ejecutó el servlet"); //verificamos que si se ejecuto la llamada http
		}
	
	}
