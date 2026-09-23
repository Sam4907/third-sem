import java.util.Scanner;
import Session3.*;
public class case4{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
HomeController controller=HomeController.getInstance();
System.out.print("\nHow many temperature commands would you like to issue? ");
int n=scanner.nextInt();
for(int i=1; i<=n; i++){
System.out.println("\nCommand #"+i+": ");
System.out.print("Enter target degrees: ");
int degrees=scanner.nextInt();
System.out.print("Enter mode (e.g., Eco, Boost) or type 'none': ");
String mode=scanner.next();            controller.processTemperatureChange(degrees, mode);
System.out.println("Total commands logged globally: "+HomeController.commandsIssued);
}
System.out.println("\nExiting.");
}
}
