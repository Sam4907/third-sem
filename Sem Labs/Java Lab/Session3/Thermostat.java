package Session3;
public class Thermostat{
public void adjustTemperature(int degrees){
System.out.println("[Thermostat] Temperature adjusted to "+degrees+"C");
}
public void adjustTemperature(int degrees, String mode){
System.out.println("[Thermostat] Temperature adjusted to "+degrees+"C in '"+mode+"' mode");
}
}
