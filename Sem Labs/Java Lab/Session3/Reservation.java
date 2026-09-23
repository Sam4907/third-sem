package Session3;
public abstract class Reservation{
String customerName;
int partySize;
public Reservation(String n, int p){
customerName=n;
partySize=p;
}
public abstract void confirmReservation();
}
