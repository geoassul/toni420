
<!-- core, para control de flujo -->
<%@ taglib uri="http://java.sun.com/jsp/jstL/core" prefix="c" %>  
<!-- lo que conseguimos con el url es el contexto donde se encuentra el servidor,
      , el var es el nombre para la direccion del serivdor (/gerenciador/nuevaEmpresa)
      se podrá acceder dentro del html ->
<c:url value="/nuevaEmpresa" var="LinkServerNuevaEmpresa"/>

<html>
      <body>
	    <!--<form action="/gerenciador/nuevaEmpresa" method="post">-->
	    
	    <form action="&{ LinkServerNuevaEmpresa }">
	    
		  Nombre empresa : <input type="text" name="nombre" />
		  Fecha Abertura : <input type="text" name="fecha" />
		  
		  <input type="submit">
		  
	    </form>
      </body>
</html>











