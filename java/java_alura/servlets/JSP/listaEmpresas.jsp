
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEconding= "ISO-8859-1" %>

<!-- de esta manera importamos librerias que se requieres para el script de java
   con una coma(,) podemos agregar mas librerias que necesitemos-->
<%@ page import ="java.util.List"%, com.alura.gerenciador.servlet.Empresa %>

<!-- de esta manera importamos las librerias JSTL(java standard TagLib) que utiliza ciertas funciones
   java en forma de etiquetas: 
   foreach() = <prefix:foreach></prefix:foreach>
   uri, es la direccion de la libreria. prefix, es la forma en la que llamaremos al la libreria dentro
   de los tag JSTL 
   *core es el nombre de la libreria, y el prefijo "c" es la instancia dentro del tag JSTL
   -->
<! core, para control de flujo >
<%@ taglib uri="http://java.sun.com/jsp/jstL/core" prefix="c" %> 
<! fmt, para formato (internacionalizacion )>
<%@ taglib uri="http://java.sun.com/jsp/jstL/fmt" prefix="fmt" %>

<% 
   //Scriptlet
   List<Empresa> nombre = (List<Empresa>) request.getAttribute("empresas"); //casteo de una clase con objetos Empresa   
%>

<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
<body>
   
    <c:if test="${ not empty empresa }"">
       Empresa ${ empresa } registrada! <br/>
   </c:if>
   
   Lista de Empresas:
   
   <!-- De esta manera utilizamos el JSTL (java standard TagLib) -->
   
   <ul>
      <!-- tambien podemos usar Expression Language dentro de nuesto JSTL -->
      <c:foreach items= "${ empresas }" var= "empresa"> 
         <li> 
            ${ empresa.nombre } - <fmt:formatDate value = "${ empresa.fechaAbertura }" pattern = "dd/MM/yyyys"> 
            <a href="/gerenciador/mostrarEmpresa?id=${empresa.id}"> modificar </a>
            <a href="/gerenciador/eliminarEmpresa?id=${empresa.id}"> eliminar </a>
         
         </li>
      </c:foreach>
   </ul>
   
   
   <!-- ...__________________________________________________________________________________--
   Scriplet + html
   
   <ul>
      <%
	 for (Empresa empresa : listaEmpresas){ 
      %>
	    
      <li> <%= empresa.getNombre()%> </li>	

      <%
	 }
      %>
   </ul>
   ... -->
   
</body>
</html>










