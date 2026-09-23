package Session3;
public class HomeController{
public static int commandsIssued=0;
private static HomeController instance;
private Home managedHome;
static{
System.out.println("Controller online");
}
private HomeController(){
this.managedHome=new Home();
}
public static HomeController getInstance(){
if(instance==null){
instance=new HomeController();
}
return instance;
}
public void processTemperatureChange(int degrees, String mode){
commandsIssued++;
if(mode=="none"){
managedHome.getThermostat().adjustTemperature(degrees);
}
else{
managedHome.getThermostat().adjustTemperature(degrees, mode);
}
}
}
