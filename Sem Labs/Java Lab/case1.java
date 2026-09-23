import Session3.*;
import java.util.Scanner;
public class case1{
public static void main(String[] args){
double tot=0;
int count=0;
Scanner scanner=new Scanner(System.in);
char choice='y';
do{
System.out.print("Enter the preferred category: ");
int cat=scanner.nextInt();
Ticket t=new Ticket(cat);
count++;
tot+=t.getPrice();
System.out.println("Tickets booked: "+count);
System.out.println("Total: $"+tot);
System.out.println();
System.out.print("Book another? (y/n): ");
choice=scanner.next().charAt(0);
}while(choice=='y');
//• After the loop ends, use if-else to apply a discount (total above Rs.1000 gets 10% off) and print the final bill.
if(tot>1000){
tot=tot-0.1*tot;
}
System.out.println("Final Bill");
System.out.println("Number of tickets booked: "+count);
System.out.println("Total payable: $"+tot);
System.out.println("Thank you!");
}
}