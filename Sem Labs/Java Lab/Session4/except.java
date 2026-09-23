class except{
public static void main(String[] args){
System.out.println("statement1");
try{
System.out.println("This will be printed");
System.out.println(10/0);
System.out.println("This will not be printed");
}
catch(ArithmeticException e){
System.out.println("Exception caught");
}
System.out.println("statement3");
}
}