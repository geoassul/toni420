import jakarta.servlet.*; // annotation, http, entre otras librerias.

//usando anotaciones, apartir de tomcat 7 se pueden usar.
//@webServlet(urlPatterns = "/hola") //a partir de tomcat recientes no es necesario usar anotacion, se puede declarar en web.xml
public class ServletTest2 extends HttpServlet{ //exteds para que una clase utilize HTTP
	
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
/*
 * hola! alura parte 2
___
-en eclipse para crear un nuevo proyecto tiene que ser de tipo Servlet

-en la nueva version de tomcat, no es necesario usar la anotacion webServlet.

-parametros en las url van definidas en la url despues del simbolo "?"
 tendrá esta forma:
   "http://localhost:8080/miproyecto/nameURL?parameter1=value"
 con el simbolo "&" colocamos mas parámetros.
-con request("request.getParameter()") podemos obtener un parametro en el arguemento
 irá el nombre del parametro.

-dentro de la carpeta web-inf esta el archivo web.xml, alli podemos declarar
 algunas caracteristicas de la url, por ejemplo el nombre que tendrá la direccion
 url y con esto ademas podemos evitar usar algunas anotacion 
 como la de "webServlet".

.. exactamente se escribirá así:
<servlet-mapping>
  <servlet-name> NuevaEmpresaServlet </serlet-name> //nombre del proyecto servlet
  <url-pattern> /nuevaEmpresa </url-pattern> // aqui va el nombre que tendra en la direccion url
</servlet-mapping>
*/
