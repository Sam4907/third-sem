package JavaLab;
class Prog11
{
	public static void main(String[] args)
	{
		byte b1 = 100;//ok
		int i = 100;//ok
		byte b2 = (byte)i;//ok
		byte b3 = (byte)130;//ok
		byte b4 = (byte)300;//ok
		
		System.out.println("b1 contains "+b1); //100
		System.out.println("b2 contains "+b2);	//100
		System.out.println("b3 contains "+b3); //-126
		System.out.println("b4 contains "+b4);	//44
	}
}