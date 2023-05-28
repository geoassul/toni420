package com.latam.alura.tienda.utils;

import javax.persistence.EntityManager;
import javax.persistence.EntityManagerFactory;
import javax.persistence.Persistence;

public class JPAUtils {
	//crea la entidad implementada en persistence.xml y POM.xml
	private static EntityManagerFactory FACTORY = Persistence.createEntityManagerFactory("tienda");
	
	// obtiene la implementacion luego de hacer el FACTORY
	public static EntityManager getEntityManager() {
		return FACTORY.createEntityManager();
	}
}
