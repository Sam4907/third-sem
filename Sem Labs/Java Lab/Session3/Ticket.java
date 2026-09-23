package Session3;
public class Ticket{
private double price; 
private int category;
public Ticket(int cat){
switch(cat){
case 1:
price=120;
break;
case 2:
price=180;
break;
case 3: 
price=250;
break;
}
}
public double getPrice(){
return price;
}
}