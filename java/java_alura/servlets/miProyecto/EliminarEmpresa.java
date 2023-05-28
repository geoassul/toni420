
package com.alura.gerenciador.servlet;

import jakarta.servlet.*;
import java.io.IOException;

public class EliminarEmpresa extends httpServlet {
	private static final long SerialVersionUID = 1l;
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response){
		
		//Obtenemos un id de la BD,el getParameter siempre devuelve un string.
		String paramId = request.getParameter("id");
		Integer id = Integer.valueof(paramId);
		
		System.out.println(id);
		
		DB db = new DB();
		db.eliminarEmpresa(id);		
		
		response.sendRedirect("listaEmpresas");
		
		}
	
	}















