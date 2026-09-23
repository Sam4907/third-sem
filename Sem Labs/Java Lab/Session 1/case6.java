//Simulate a vending machine with a menu (1-Coffee ₹10, 2-Tea ₹8, 3-Juice ₹15, 4-Water ₹5). 
//Read choice using switch, read amount inserted, calculate change or ask for more money using while loop.

import java.util.Scanner;
public class case6{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter your choice: ");
int choice=scanner.nextInt();
int price=0;
switch(choice){
	case 1:
		System.out.println("You selected coffee! It is $10");
		price=10;
break;
case 2:
		System.out.println("You selected tea! It is $8");
price=8;
break;
case 3:
		System.out.println("You selected juice! It is $15");
price=15;
break;
case 4:
		System.out.println("You selected water! It is $5");
price=5;
break;
default:
System.out.println("Enter a valid choice");
return;
}

int am=0;
while(true){
System.out.print("Enter the amount: ");
am+=scanner.nextInt();
if(am>=price){
System.out.println("Change: $"+(am-price));
break;
}
else{
System.out.println("Enter $"+(price-am)+" more!");
}
}
}
} 