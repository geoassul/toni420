package com.latam.alura.tienda.prueba;

import java.math.BigDecimal;

import javax.persistence.EntityManager;

import com.latam.alura.tienda.dao.CategoriaDao;
import com.latam.alura.tienda.dao.ProductoDao;
import com.latam.alura.tienda.modelo.Categoria;
import com.latam.alura.tienda.modelo.Producto;
import com.latam.alura.tienda.utils.JPAUtils;

public class RegistroDeProducto {

	public static void main(String[] args) {
	    registrarProducto();
	    //luego de registrar el producto y inicializar la conexion con hibernate se solicita una conexion a la bae de datos con getEntity
	    EntityManager em = JPAUtils.getEntityManager();
	    ProductoDao productoDao = new ProductoDao(em);
	    // imprimir en pantalla el nombre del item registrado en la clase producto
	    Producto producto = productoDao.consultaPorId(1l);
	    System.out.println(producto.getNombre());
	    
	    BigDecimal precio = productoDao.consultarPrecioPorNombreDeProducto("Xiaomi Redmi");
	    System.out.println(precio);
	    //el tipo de datos consultado es el mismo que está en la base de datos(correlación)

	}

	private static void registrarProducto() {
	    
	    //datos que se registraran en la clase producto y categoria.
	    Categoria celulares = new Categoria("CELULARES");
	    Producto celular = new Producto("Xiaomi Redmi", "Muy bueno", new BigDecimal("800"), celulares);
	    
	    //invocando a hibernate para conexion mediante h2
	    EntityManager em = JPAUtils.getEntityManager();
	    
	    //conectando la clase DAO a hibernate(em)
	    ProductoDao productoDao = new ProductoDao(em);
	    CategoriaDao categoriaDao = new CategoriaDao(em);
        
	
	    //funcion para iniciar ORM ( object relational mapping)
	    em.getTransaction().begin();
	    
	    //enviando los datos al DAO para manipular con hibernate mediante DAO
	    categoriaDao.guardar(celulares);
	    productoDao.guardar(celular);	
	    
	    //inciando la transaccion con hibernate
	    em.getTransaction().commit();
	    em.close();
	}

}








