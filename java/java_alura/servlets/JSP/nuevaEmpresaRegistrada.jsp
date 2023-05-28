<!--
<!Java Server Page - JSP>
<!este trozo de codigo se le conoce como ScriptLet.>
<% 
   //obitene un valor que se envio del servlet con el alias requerido
   String empresa = (String) request.getAttribute("empresa"); //String castea al resultado request(object)
   System.out.println(empresa);
%>

<! html >
<html >
<body>
   <!esto es igual que utilizar el PrintWriter.. out.print(empresa)">
   
   mi mensaje paso al html: <%= empresa %> , es el resultado 
   primer projecto con Servlet - Curso Alura.
   
</body>
</html>
-->

<! tambien podemos escribir el html usando EXPRESIONES >
<!-- lo que sucede es debido al RequestDispatcher que hizo la conexion con
   este jsp que nos envió el valor del objeto empresa, con la EXPRESION
   solamente utilizamos esos parametros enviados.-->

<%@ taglib uri="http://java.sun.com/jsp/jstL/core" prefix="c" %>  

<html>
 <body>
    <c:if test="${ empty empresa }">
       ninguna empresa registrada!
    </c:if>
    <c:if test="${ not empty empresa }">
       empresa ${ empresa } registrada!
    </c:if>
 </body>
</html>
















