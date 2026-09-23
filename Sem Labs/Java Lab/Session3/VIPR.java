package Session3;
public class VIPR extends Reservation{
public VIPR(String n, int p){
super(n, p);
}
@Override
public void confirmReservation(){
System.out.println("Your hold time is 30 minutes");
}
}