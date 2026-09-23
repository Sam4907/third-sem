package JavaLab;
class Rectangle
{
	int length,breadth;
	public void setParam(int l,int b)
	{
		length=l;
		breadth=b;
	}
	/*getter methods are generally nonvoid methods,does not require 
		any argument list 
	process on fields of objects*/
	public double getArea()
	{
		return length*breadth;
	}
	public double getPerimeter()
	{
		return 2*(length+breadth);
	}
}
class Prog28
{
	public static void main(String[] args)
	{
		Rectangle r = new Rectangle();
		
		r.setParam(20,50);
		
		System.out.println("Area of rectangle r is "+r.getArea()+" perimeter is "+r.getPerimeter());
	}
}