import jakarta.servlet.ServletException;

public class ListaEmpresasServlet {
	
	private static final long serialVersionUID = 1l;
	
	//con service podemos usar get y post
	protected void service (httpServletRequest request , HttpServletResponse response) 
			throws ServletException, IOException{
		
		DB baseDeDatos = new DB();
		list<Empresa> listaEmpresas = baseDeDatos.getEmpresa();
		
		//conectamos al JSP
		request.setAttribute("empresas",listaEmpresas);
		RequestDispatcher rd = request.getRequestDispatcher("/listaEmpresas.jsp");
		rd.forward(request,response);
		
		}
	
	}






















