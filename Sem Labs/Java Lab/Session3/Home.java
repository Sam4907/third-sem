package Session3;
public class Home{
private Thermostat thermostat;
public Home(){
this.thermostat=new Thermostat();
System.out.println("[Home] New home built with an integrated thermostat");
}
public Thermostat getThermostat(){
return this.thermostat;
}
}