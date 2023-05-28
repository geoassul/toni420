package ...;
import jakarta.servlet.*;
import java.io.IOException

public class MostrarEmpresaServlet extends HttpServlet {
	
	private static final long serialVersionUID = 1l;
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		
		String paramId = request.getParameter("id");
		Integer id = Integer.valueOf(paramId);
		
		System.out.println(id);
		
		DB db = new DB();
		empresa emp = db.buscarEmpresaPorId(id);		
		
		System.out.println(emp.getNombre());
		
		request.SetAttribute("empresa",emp);
		
		RequestDispatcher rd = request.getRequestDispatcher("/listaEmpresas.jsp");
		rd.forward(request,response);
		
		}
		
		
		
	}





















