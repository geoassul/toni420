class Cuenta_clase{
	
	double saldo;
	int agencia;
	int numero;
	datosTitular titular = new datosTitular();
	
	public void deposito( double valor){
		this.saldo = this.saldo + valor;
		//System.out.println(this.saldo);
		}
	
	public boolean retirar( double valor){
		if (valor <= this.saldo){
			this.saldo = this.saldo - valor;
			System.out.println(this.saldo);
			return true;  //es necesario usar return si el metodo tiene retorno
			}
		else {
			return false;
			}
			
		}
	public boolean transferir(double valor, Cuenta_clase nombreCuenta){
		if (valor <= this.saldo){
			this.saldo = this.saldo - valor;
			nombreCuenta.deposito(valor);
			System.out.println("hizo un deposito de: " + valor);
			return true;
			}
		return false;
		}
		
	public double obtenerSaldo(){
		return this.saldo;
		}
	}
