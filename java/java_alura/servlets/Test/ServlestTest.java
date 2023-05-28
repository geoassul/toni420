import jakarta.servlet.*;

//hola
//usando anotaciones, apartir de tomcat 7 se pueden usar.
@webServlet(urlPatterns = "/hola") //esto modifica el nombre la ubicacion del archivo html en la direccion url
public class ServlestTest extends HttpServlet{ //exteds para que una clase utilize HTTP
	
	@override //es porque modificaremos el metodo de la clase padre
	protected void service(HttpServletRequest req, HttpServletResponse resp) throws IOException{ //request y response
			//con http podemos enviar String o HTML
			PrintWriter out = resp.getWriter() // un output que envia datos html
			out.println("<html>"); // de esta manera usamos el objeto out. 
			out.println("<body>");// println envia html con un salto de linea al final 
			out.println("hola mundo! enviando mi primer texto con html mediante http");
			out.println("</body>");
			out.println("</html>");
			
			System.out.println("Se ejecutó el servlet"); //verificamos que si se ejecuto la llamada http
		}
	
	}
/*
 * hola! alura parte 1
______
-tomcat es un servidor web java
 http://localhost:8080 es la url por defecto que se ejecuta tomcat
-el proyecto desarrollado en java el parte de la url
 http://localhost:8080/Mi_proyecto_java 
-para mapear la url a un serlet se usa la anotacion @WebServlet
-un servlet debe extender la clase HttpServlet

___--
-service se encarga de la comunicacion http.
-webServlet es una anotacion que permite la comuncacion con la JVM
 ademas wevServlet marca la calse como Servlet y con el parámetro 
 urlPatterns modificamos y registramos la direccion url.
-request y response:
	-response es la respuesta, en http se pueden enviar dos tipos de datos
	stream de datos y enviar html directamente.
	
de la siguente forma se crean las direcciones url con Servlet
protocolo://ip:puerta/contexto/recurso
* */
