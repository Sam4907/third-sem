import java.util.Scanner;
//A power company charges: ₹0-100 units → ₹0/unit free, 101-200 units → ₹5/unit, 
// 201-300 units → ₹7/unit, above 300 → ₹10/unit. Read units consumed and print the total 
// bill using if-else/switch. 
public class case1{
    public static void main(String[] args){
        int amount;
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter the number of units: ");
        int units=scanner.nextInt();
        if(units>=0&&units<=100){
            System.out.println("Amount: $" + (units*0));
        }
        else if(units>100&&units<=200){
	    System.out.println("Amount: $" + (units*5));
	}
	else if(units>200&&units<=300){
	    System.out.println("Amount: $" + (units*7));
	}
	else{
	    System.out.println("Amount: $" + (units*10));
	}
    }
}
