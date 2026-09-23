package Session3;
public class RR extends Reservation{
public RR(String n, int p){
super(n, p);
}
@Override
public void confirmReservation(){
System.out.println("Your hold time is 15 minutes");
}
}