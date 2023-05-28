package com.mycompany.app;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Table;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.Configuration;

@Entity
@Table(name = "employees")
class Employee {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private int id;
    private String firstName;
    private String lastName;

    public Employee() {}

    public Employee(String firstName, String lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public int getId() {
        return id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}

public class App {
    public static void main(String[] args) {
        // Create the Hibernate configuration object
        Configuration config = new Configuration();
        config.addAnnotatedClass(Employee.class);
        config.setProperty("hibernate.connection.driver_class", "org.sqlite.JDBC");
        config.setProperty("hibernate.connection.url", "jdbc:sqlite:test.db");
        config.setProperty("hibernate.dialect", "com.zsoltfabok.sqlite.dialect.SQLiteDialect");

        // Create the session factory
        SessionFactory sessionFactory = config.buildSessionFactory();

        // Create a new employee and save it to the database
        Session session = sessionFactory.openSession();
        session.beginTransaction();
        Employee employee = new Employee("John", "Doe");
        session.save(employee);
        session.getTransaction().commit();
        session.close();

        // Retrieve the employee from the database and print its details
        session = sessionFactory.openSession();
        Employee retrievedEmployee = session.get(Employee.class, employee.getId());
        System.out.println("Employee ID: " + retrievedEmployee.getId());
        System.out.println("First Name: " + retrievedEmployee.getFirstName());
        System.out.println("Last Name: " + retrievedEmployee.getLastName());
        session.close();

        // Close the session factory
        sessionFactory.close();
    }
}
