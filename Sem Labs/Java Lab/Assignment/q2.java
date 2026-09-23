import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

class Employee{
private int baseSalary;
private int performanceScore;
public Employee(int baseSalary,int performanceScore){
this.baseSalary=baseSalary;
this.performanceScore=performanceScore;
}
public int getBaseSalary(){
return baseSalary;
}
public int getPerformanceScore(){
return performanceScore;
}
}

interface PayrollStrategy{
double calculateBonus(Employee employee);
}

class ManagerBonusStrategy implements PayrollStrategy{
public double calculateBonus(Employee employee){
return (employee.getBaseSalary()*0.20)+(employee.getPerformanceScore()*1000);
}
}

class EngineerBonusStrategy implements PayrollStrategy{
public double calculateBonus(Employee employee){
return employee.getBaseSalary()*0.10;
}
}

class InternBonusStrategy implements PayrollStrategy{
public double calculateBonus(Employee employee){
return 500.0;
}
}

class PayrollCalculator{
private Map<String,PayrollStrategy> strategies=new HashMap<>();
public void registerStrategy(String designation,PayrollStrategy strategy){
strategies.put(designation.toLowerCase(),strategy);
}
public double computeBonus(Employee employee,String designation){
PayrollStrategy strategy=strategies.get(designation.toLowerCase());
if(strategy==null){
throw new IllegalArgumentException("Invalid designation!");
}
return strategy.calculateBonus(employee);
}
}

public class q2{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
PayrollCalculator calculator=new PayrollCalculator();
calculator.registerStrategy("manager",new ManagerBonusStrategy());
calculator.registerStrategy("engineer",new EngineerBonusStrategy());
calculator.registerStrategy("intern",new InternBonusStrategy());
System.out.print("Enter number of employees: ");
int n=scanner.nextInt();
for(int i=0; i<n; i++){
System.out.println("Enter details for employee "+(i+1));
System.out.print("Enter designation (manager/engineer/intern): ");
String designation=scanner.next();
System.out.print("Enter base salary: ");
int baseSalary=scanner.nextInt();
System.out.print("Enter performance score: ");
int performanceScore=scanner.nextInt();
Employee employee=new Employee(baseSalary,performanceScore);
try{
double bonus=calculator.computeBonus(employee,designation);
System.out.println("Calculated Bonus: "+bonus);
}
catch(IllegalArgumentException e){
System.out.println(e.getMessage());
}
System.out.println();
}
}
}
