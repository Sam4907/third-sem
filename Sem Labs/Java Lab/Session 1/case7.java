//A bank checks loan eligibility: read monthly income and requested EMI amount. 
//If EMI exceeds 40% of income, reject; else approve. Use a loop to check eligibility for multiple applicants (read count first). 

import java.util.Scanner;
public class case7{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter the number of applicants: ");
int n=scanner.nextInt();
for(int i=0; i<n; i++){
System.out.println("Enter details of applicant "+(i+1));
System.out.print("Enter monthly income: ");
int mi=scanner.nextInt();
System.out.print("Enter EMI: ");
int emi=scanner.nextInt();
if(emi>(0.4*mi)){
System.out.println("Rejected!");
}
else{
System.out.println("Accepted!");
}
System.out.println();
}
}
}