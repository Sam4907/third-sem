import java.util.Scanner;
import java.util.Arrays;
public class case1{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter the number of accounts: ");
int n=scanner.nextInt();
int count=0;
Account[] accs=new Account[n];
for(int i=0; i<n; i++){
System.out.println("Enter details for account "+(i+1)+":");
System.out.print("Enter account holder name: ");
String name=scanner.next();
System.out.print("Enter account number: ");
int num=scanner.nextInt();
System.out.print("Enter initial deposit: ");
int in=scanner.nextInt();
Account acc=new Account(name, num, in);
if(acc.balance!=0){
accs[i]=acc;
count++;
}
}
accs=Arrays.copyOf(accs, count); 
System.out.println("Summary for "+accs.length+" accounts: ");
for(int i=0; i<accs.length; i++){
System.out.println("Details for account"+(i+1)+" :");
System.out.println("Account holder name: "+accs[i].holdern);
System.out.println("Account number: "+accs[i].accountn);
if(accs[i].balance==0){
System.out.println("Account could not be created!");
}
else{
System.out.println("Account balance: "+accs[i].balance);
}
System.out.println();
}
}
}


class Account{
String holdern;
int accountn;
int balance=0;
Account(String name, int num, int ini){
	holdern=name;
	accountn=num;
	balance=ini;
	if(ini<500){
		System.out.println("Account cannot be created");
		balance=0;
	System.out.println();
}
	else{
		System.out.println("Account created successfully!");
System.out.println();	
}
}
}