
public class CuentaAhorro extends Cuenta{
	
	public CuentaAhorro(int agencia, int numero){
		super(agencia,numero);
		}
	
	public void deposita(double valor){
		this.saldo = this.saldo + valor;
		}
}

