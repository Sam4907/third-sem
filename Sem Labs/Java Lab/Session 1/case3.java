//Read marks of 5 subjects for a student. Compute total, percentage, and assign grade (A/B/C/D/F) using if-else. 
//Use a loop to take input for 5 subjects instead of separate variables. 

import java.util.Scanner;
public class case3{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
int sum=0;
int[] arr=new int[5];
for(int i=0; i<5; i++){
System.out.print("Enter marks of subject"+(i+1)+": ");
int val=scanner.nextInt();
arr[i]=val;
}
for(int i: arr){
sum+=i;
}
float perc=sum/5;
System.out.println("Total: "+sum);
System.out.println("Percentage: "+perc);
if(perc>90){
System.out.println("Grade A");
}
else if(perc>75){
System.out.println("Grade B");
}
else if(perc>55){
System.out.println("Grade C");
}
else if(perc>33){
System.out.println("Grade D");
}
else{
System.out.println("Grade F");
}
}
}