package JavaLab;
import java.util.Scanner;
class Fourth
{
	public static int abs(int no) 
	{
		if(no>0)
		return no;
		else
		return -no;
	}
	public static void main(String[] args)
	{
		Scanner scanner=new Scanner(System.in);
		System.out.print("Enter a number: ");
		 int no = scanner.nextInt();
		
		 no = Fourth.abs(no); 
		System.out.println("absolute of given no. is " +no );
	}
}