package JavaLab;
import java.util.Scanner;
//prog19
class Second
{
	public static void main(String[] args)
	{
		Scanner scanner=new Scanner(System.in);
		System.out.print("Enter a year: ");
		int yr=scanner.nextInt();
		if(yr%4==0 && yr%100!=0){
			System.out.println(yr+" is a leap year");
		}
		else{
			System.out.println(yr+" is not a leap year");
		}
	}
}