//Simulate an ATM. User enters withdrawal amount. Check if amount is a multiple of 100, 
//check if it exceeds balance (assume balance = ₹10000), then compute minimum number of ₹2000, ₹500, ₹100 notes needed using loops. 
import java.util.Scanner;

public class case2{
	public static void main(String[] args){
		Scanner scanner=new Scanner(System.in);
		int balance=10000;
		int two=0, five=0, one=0;
		System.out.print("Enter the amount: ");
		int amount=scanner.nextInt();
		if(amount>balance){
			System.out.println("Insufficient Balance. Available balance: $"+ balance);
			return;
}
		if(amount%100!=0){
			System.out.println("Try again with a multiple of 100!");
}
		else{
			while(amount>0){
				if(amount>1999){
					amount-=2000;
					two++;
}	
				else if(amount>499){
					amount-=500;
					five++;
}
				else{
					amount-=100;
					one++;
}
}
			System.out.println("Amount withdrawn: ");
			System.out.println("Number of $2000 bills: "+ two);
			System.out.println("Number of $500 bills: "+ five);
			System.out.println("Number of $100 biils: "+ one);
		}
}
}