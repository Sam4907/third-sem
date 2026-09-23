package JavaLab;
import java.util.Scanner;

class Fifth
{
	public static void main(String[] args)
	{
		Scanner scanner=new Scanner(System.in);
		System.out.print("Enter a number: ");
		 int no = scanner.nextInt();
		
		if(MathUtil.isPrime(no))
		System.out.println(no+" is a prime number");
		
		else
		System.out.println(no+" is a composite number");
	
		System.out.println("sum of digits of given number is "+MathUtil.getSum(no));
	}

	private static class MathUtil {
		static boolean isPrime(int n) {
			if (n <= 1) return false;
			if (n <= 3) return true;
			if (n % 2 == 0) return false;
			int r = (int) Math.sqrt(n);
			for (int i = 3; i <= r; i += 2) {
				if (n % i == 0) return false;
			}
			return true;
		}

		static int getSum(int n) {
			int sum = 0;
			int x = Math.abs(n);
			while (x > 0) {
				sum += x % 10;
				x /= 10;
			}
			return sum;
		}
	}
}