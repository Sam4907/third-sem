package Session3;
public class Manager extends Employee{
public Manager(String n, double f){
super(n, f);
}
@Override
public double calcSalary(){
return basicPay+basicPay*0.2;
}
}