package com.latam.alura.tienda.modelo;

import java.math.BigDecimal;
import java.time.LocalDate;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.ManyToOne;
import javax.persistence.Table;

@Entity
@Table(name="productos")
public class Producto{

	@Id
	@GeneratedValue(strategy=GenerationType.IDENTITY)
	private Long id;
	
	//definiendo el tipo de datos que se encuentran tambien con el mismo tipo de datos en la base de datos.
	private String nombre;
	private String descripcion;
	private BigDecimal precio;
	private LocalDate fechaDeRegistro= LocalDate.now();
	
	//anotacion para realizar un innerjoin (relacionamiento del id de categoria con el id
	@ManyToOne
	private Categoria categoria;

	
	public Producto() {
		
	}
	public Producto(String nombre, String descripcion, BigDecimal precio, Categoria categoria) {
		this.nombre = nombre;
		this.descripcion = descripcion;
		this.precio = precio;
		this.categoria = categoria;
	}
	public Long getId() {
		return id;
	}

	public String getNombre() {
		return nombre;
	}
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	public String getDescripcion() {
		return descripcion;
	}
	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}
	public BigDecimal getPrecio() {
		return precio;
	}
	public void setPrecio(BigDecimal precio) {
		this.precio = precio;
	}
}
