import Session3.*;
import java.util.Scanner;
public class case2{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter the number of reservations: ");
int n=scanner.nextInt();
for(int i=0; i<n; i++){
System.out.print("Enter your name: ");
String nm=scanner.next();
System.out.print("Enter the party size: ");
int p=scanner.nextInt();
System.out.print("Enter type (V/R): ");
char t=scanner.next().charAt(0);
if(t=='V'){
Reservation r=new VIPR(nm, p);
r.confirmReservation();
}
else{
Reservation r=new RR(nm, p);
r.confirmReservation();
}

}
}
}