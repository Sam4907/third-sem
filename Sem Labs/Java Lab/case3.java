import java.util.Scanner;
import Session3.*;
public class case3{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
char choice='y';
do{
System.out.print("Enter employee name: ");
String n=scanner.next();
System.out.print("Enter basic pay: ");
double s=scanner.nextDouble();
System.out.print("Manager or Developer? (M/D): ");
char c=scanner.next().charAt(0);
if(c=='M'){
Employee e=new Manager(n, s);System.out.println("Salary: "+e.calcSalary());
}
else{
System.out.print("Enter number of projects completed: ");
int p=scanner.nextInt();
Employee e=new Developer(n, s, p);
System.out.println("Salary: "+e.calcSalary());
}
System.out.print("Enter more employees? (y/n): ");
choice=scanner.next().charAt(0);
System.out.println();
}while(choice=='y');
}
}