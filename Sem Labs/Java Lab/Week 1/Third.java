package JavaLab;
import java.util.Scanner;

public class Third {
	public static void main(String[] args)
	{
        Scanner scanner=new Scanner(System.in);
        System.out.print("Enter a character: ");
		String inp = scanner.nextLine();
        char ch=inp.charAt(0);	
		if(Character.isUpperCase(ch))
		System.out.println(ch+" is a upper case letter");
		
		else if(Character.isLowerCase(ch))
		System.out.println(ch+" is a lower case letter");
		
		else if(Character.isDigit(ch))
		System.out.println(ch+" is a digit");
		
		else
		System.out.println(ch+" is a special character/symbol");
        scanner.close();
	}
}

