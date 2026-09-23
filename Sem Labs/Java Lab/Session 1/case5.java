//A shop wants a triangle-shaped LED display pattern (of stars or numbers) for Diwali decoration. 
//Take number of rows as input and print the pyramid pattern using nested for loops. 

import java.util.Scanner;
public class case5{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter the number of row: ");
int n=scanner.nextInt();
for(int i=1; i<=n; i++){
for(int j=1; j<=n-i; j++){
                System.out.print(" ");
            }
for(int k=1; k<=(2*i-1); k++){
                System.out.print("*");
            }
System.out.println();
}
}
}