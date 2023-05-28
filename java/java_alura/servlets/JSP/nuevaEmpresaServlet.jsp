
<% 
   list<String> nombre = request.getAttribute("empresa");
   
%>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<body>
    our.println("<html><body>");
    our.println("<ul>");
    for (Empresa empresa : listaEmpresas){ //esto foritera sobre la lista dentro de BD
	    our.println("<li>" + empresa.getNombre()+"</li>");
	    }
    our.println("</ul>");
    our.println("</body></html>");
    
	
</body>
</html>

















