public class Cliente implements Autenticable{

    private AutenticacionUtil util;
    private String nombre;
    private String numeroIdentidad;
    private String profesion;
    
    public Cliente{
        this.util = new AutenticacionUtil();
        }

    public String getNombre() {
        return nombre;
    }
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }
    public String getNumeroIdentidad() {
        return numeroIdentidad;
    }
    public void setNumeroIdentidad(String numeroIdentidad) {
        this.numeroIdentidad = numeroIdentidad;
    }
    public String getProfesion() {
        return profesion;
    }
    public void setProfesion(String profesion) {
        this.profesion = profesion;
    }
    
    @Override
    public void setClave(String clave){
        this.util.setClave(clave);
        }

    @Override
    public boolean iniciarSesion(String clave){
        return this.util.iniciarSesion(clave);
        }

}
