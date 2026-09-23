//A car's fuel starts at 50 litres and consumes 5 litres per 100 km. 
//Using a while loop, keep printing remaining fuel after every 100 km driven, and print "Refuel needed" when fuel drops below 10 litres. 

public class case8{
public static void main(String []args){
int curr=50, dist=0;
while(curr>10){
	dist+=100;
	curr-=5;
	System.out.println("Distance: "+dist);
	System.out.println("Remaining fuel: "+curr);
}
System.out.println("Refuel needed!");
}
}