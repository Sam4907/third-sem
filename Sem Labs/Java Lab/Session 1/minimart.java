import java.util.Scanner;

public class minimart{
    public static void display(){
        System.out.println("MiniMart Menu: ");
        System.out.println("1. Add item to cart");
        System.out.println("2. View Bill");
        System.out.println("3. Apply discount");
        System.out.println("4. Print Reciept Pattern");
        System.out.println("5. Exit");
        System.out.println();
    }
    public static void pattern(){
        for(int i=1; i<=4; i++){
            for(int j=1; j<=i; j++){
                System.out.print("* ");
            }
            System.out.println();
        }
        System.out.println("Thank you for shopping!");
    }
    public static void applydisc(double total){
        double discountAmount=0;
        int disc=0;   
        if(total>1000){
            discountAmount=total*0.1;
            disc=10;
        }
        else if(total>500){
            discountAmount=total*0.05;
            disc=5;
        }
        double finalTotal=total-discountAmount;
        System.out.println("Discount applicable: "+disc+"%");
        System.out.println("After discount: "+finalTotal);
    }
    public static void endroutine(double total, String[] items, double[] quants, double[] price, int count){
        int points=0;
        double co=total;
        double discountAmount=0;
        int disc=0;   
        if(total>1000){
            discountAmount=total*0.1;
            disc=10;
        }
        else if(total>500){
            discountAmount=total*0.05;
            disc=5;
        }
        double finalTotal=total-discountAmount;
        double cop=finalTotal;
        while(cop>0){
                cop-=10;
                points++;
            }
        System.out.println("---BILL---");
        for(int i=0; i<count; i++){
            System.out.println(items[i]+" x "+quants[i]+" = Rs. "+price[i]);
        }
        System.out.println("Total= "+co);
        System.out.println("Discount applicable: "+disc+"%");
        System.out.println("After discount: "+finalTotal);
        System.out.println("Loyalty points: "+points);
        pattern();
    }
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);
        int choice=0;
        double total=0;
        double am=0;
        int i=0;
        String[] lst=new String[10];
        double[] quant=new double[10];
        double[] price=new double[10];
        do{
            if(i==10){
                System.out.println("Limit reached!");
                endroutine(total, lst, quant, price, i);
                break;
            }
            display();
            System.out.print("Enter your choice: ");
            choice=scanner.nextInt();
            switch(choice){
                case 1: 
                    System.out.println("1. Rice ($50/kg)");
                    System.out.println("2. Sugar ($40/kg)");
                    System.out.println("3. Oil ($120/l)");
                    System.out.println("4. Milk ($25/l)");
                    System.out.print("Enter your choice: ");
                    int item=scanner.nextInt();
                    System.out.print("Enter the quantity: ");
                    double q=scanner.nextDouble();
                    quant[i]=q;
                    switch(item){
                        case 1:
                            am=50*q;
                            lst[i]="Rice";
                            break;
                        case 2:
                            am=40*q;
                            lst[i]="Sugar";
                            break;
                        case 3:
                            am=120*q;
                            lst[i]="Oil";
                            break;
                        case 4:
                            am=25*q;
                            lst[i]="Milk";
                            break;
                        default:
                            System.out.println("Invalid item choice!");
                            continue;
                    }
                    total+=am;
                    price[i]=am;
                    i++;
                    break;
                case 2: 
                    endroutine(total, lst, quant, price, i);
                    break;
                case 3: 
                    applydisc(total);
                    break;
                case 4:
                    pattern();
                    break;
                case 5:
                    System.out.println("Exiting!");
                    endroutine(total, lst, quant, price, i);
                    break;  
                default:
                    System.out.println("Enter a valid choice!");
            }
        }while(choice!=5);
    }
}