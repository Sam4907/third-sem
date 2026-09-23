package Session3;
public class Employee{
protected String name;
protected double basicPay;
public Employee(String n, double b){
name=n;
basicPay=b;
}
public double calcSalary(){
return basicPay;
}
}