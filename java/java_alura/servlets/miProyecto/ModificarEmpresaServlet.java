
package com.alura.gerenciador.servlet;

import jakarta.servlet.*;
import java.io.IOException;

public class ModificarEmpresaServlet extends HttpServlet {
	private static final long SerialVersionUID = 1l;
	
	protected void doPost(HttpServletRequest request, HttpServletResponse response){
		
		System.out.println("Empresa modificada");
		
		String nombreEmpresa = request.getParameter("nombre"); 
		String paramFechaAbertura = request.getParameter("fecha"); 
		String paramId = request.getParameter("id");
		Integer id = Integer.valueOf(paramId);
		
		System.out.println(id);
		
		Date fechaAbertura = null; 
		try{
			SimpleDateFormat sdf = new SimpleDateFormat("dd/MM/yyyy");
			fechaAbertura = sdf.parse(paramFechaAbertura);
		} catch(ParseException e) {
			throw new ServletException(e);
			}
		
		DB db = new DB();
		Empresa empresa = db.buscarEmpresaPorId(id);
		empresa.setNombre(nombreEmpresa);
		empresa.setFechaAbertura(fechaAbertura);
		
		//redireccionamiento
		response.sendRedirect("listaEmpresas");
			
		}	
	
	}




















