package Session3;
public class Developer extends Employee{
int projectsCompleted;
public Developer(String n, double f, int p){
super(n, f);
projectsCompleted=p;
}
@Override
public double calcSalary(){
if(projectsCompleted>5){
return basicPay+basicPay*0.15;
}
else{
return basicPay+basicPay*0.08;
}
}
}