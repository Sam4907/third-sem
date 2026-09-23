import java.util.Scanner;
public class case2{
public static void display(){
System.out.println("Menu");
System.out.println("1. Idli- $40");
System.out.println("2. Dosa- $60");
System.out.println("3. Coffee- $20");
System.out.println("4. Juice- $50");
}
public static void main(String[] args){
char more='y';
int total=0;
Scanner scanner=new Scanner(System.in);
do{
display();
System.out.print("Enter your choice: ");
int choice=scanner.nextInt();
switch(choice){
case 1: 
total+=40;
break;
case 2:
total+=60;
break;
case 3:
total+=20;
break;
case 4:
total+=50;
break;
default:
System.out.println("Enter a valid choice!");
}
System.out.print("Order more? (y/n): ");
more=scanner.next().charAt(0);
System.out.println();
}while(more=='y');
double ne=total;
int disc=0;
if(total>300){
ne=total-(total*0.1);
disc=10;
}
else if(total>150){
ne=total-(total*0.05);
disc=5;
}
System.out.println("Bill: ");
System.out.println("Total amount: $"+total);
System.out.println("Discount applied: "+disc+"%");
System.out.println("Total payable: $"+ne);
}
}
class MenuItem{
String item;
double price;
MenuItem(String name, double p){
	item=name;
	price=p;
}
}