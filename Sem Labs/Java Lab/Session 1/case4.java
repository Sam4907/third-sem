//A bus charges fare based on distance: 0-5 km ₹10, 6-10 km ₹20, 11-20 km ₹35, 
// above 20 km ₹50. Read distance and number of passengers, compute total fare 
// using switch (on distance range converted to a case code) and a loop for multiple passengers. 

import java.util.Scanner;

public class case4{
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
	System.out.print("Enter the distance: ");
	int dist=scanner.nextInt();
	System.out.print("Enter the number of passengers: ");
	int pass=scanner.nextInt();
	switch(dist){
		case 0, 1, 2, 3, 4, 5->System.out.println("Amount: $"+(10*pass));
		case 6, 7, 8, 9, 10->System.out.println("Amount: $"+(20*pass));
	case 11, 12, 13, 14, 15, 16, 17, 18, 19, 20->System.out.println("Amount: $"+(35*pass));
		default->System.out.println("Amount: $"+(50*pass));

}
    }
}