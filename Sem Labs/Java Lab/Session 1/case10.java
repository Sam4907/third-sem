//A cashier receives a total cash amount to be broken into denominations of ₹500, ₹200, ₹100, ₹50, ₹20, ₹10. 
//Read the amount and use a loop with modulus/division to compute how many notes of each denomination are needed. 

import java.util.Scanner;

public class case10{
    public static void main(String[] args) {
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter the total amount: ");
        int amount=scanner.nextInt();
        int[] denominations={500, 200, 100, 50, 20, 10};

        for(int note: denominations){
            int count=amount/note; 
            amount=amount%note; 
            if(count>0){
                System.out.println("$"+note+" notes: "+count);
            }
        }
        if(amount>0){
            System.out.println("Remaining change: $" + amount);
        }

        scanner.close();
    }
}