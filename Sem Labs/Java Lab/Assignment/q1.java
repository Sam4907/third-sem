import java.util.Scanner;
import java.util.UUID;

class BankTransactionException extends Exception{
private UUID txId;
public BankTransactionException(String message, UUID txId){
super(message);
this.txId=txId;
}
public UUID getTxId(){
return txId;
}
}

class InvalidAccountException extends BankTransactionException{
private String accNum;
public InvalidAccountException(String message, UUID txId, String accNum){
super(message,txId);
this.accNum=accNum;
}
public String getAccNum(){
return accNum;
}
}

class FinancialRuleException extends BankTransactionException{
public FinancialRuleException(String message,UUID txId){
super(message,txId);
}
}

class InsufficientBalanceException extends FinancialRuleException{
public InsufficientBalanceException(UUID txId){
super("Insufficient Balance!",txId);
}
}

class BankingNetworkTimeoutException extends RuntimeException{
private UUID txId;
public BankingNetworkTimeoutException(String message,UUID txId){
super(message);
this.txId=txId;
}

public UUID getTxId(){
return txId;
}
}

public class q1{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter number of transactions: ");
int n=scanner.nextInt();
for(int i=0; i<n; i++){
UUID txId=UUID.randomUUID();
System.out.println("Processing transaction "+(i+1)+" ("+txId+")");
System.out.print("Enter source account status (valid/invalid): ");
String status=scanner.next();
System.out.print("Enter balance: ");
int balance=scanner.nextInt();
System.out.print("Enter transfer amount: ");
int amount=scanner.nextInt();
System.out.print("Simulate network timeout? (true/false): ");
boolean timeout=scanner.nextBoolean();
try{
if(status.equals("invalid")){
throw new InvalidAccountException("Account is invalid!",txId,"SRC-ERR");
}
if(amount>balance){
throw new InsufficientBalanceException(txId);
}
if(timeout){
throw new BankingNetworkTimeoutException("Network connection lost!",txId);
}
System.out.println("Transaction Completed Successfully!");
}
catch(InvalidAccountException e){
System.out.println("Security Alert: "+e.getMessage()+" Account: "+e.getAccNum());
}
catch(InsufficientBalanceException e){
System.out.println("Transaction Rejected: "+e.getMessage());
}
catch(BankingNetworkTimeoutException e){
System.out.println("Critical Error: "+e.getMessage()+" Sending to reconciliation queue.");
}
System.out.println();
}
}
}
