package JavaLab;
class tenth
{
	static int a=10,b;
	public static void jf(int c)
	{
		System.out.println("Invocation of jf()");
		System.out.println("a= "+a);
		System.out.println("b= "+b);
		System.out.println("c= "+c);
	}
	public static void main(String[] args)
	{
		System.out.println("Invocation of main()");
		jf(100);
	}
	static
	{
		System.out.println("Inside the 1st static block");
	}
	static
	{
		System.out.println("Inside the 2nd static block");
		b=a*5;
		jf(200);
	}
}