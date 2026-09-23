import java.util.Scanner;
public class case3{
public static void main(String[] args){
Scanner scanner=new Scanner(System.in);
System.out.print("Enter the number of students: ");
int n=scanner.nextInt();
Student[] ss=new Student[n];
for(int i=0; i<n; i++){
System.out.println("Enter details for student "+(i+1)+":");
System.out.print("Enter student name: ");
String name=scanner.next();
System.out.print("Enter roll number: ");
int num=scanner.nextInt();
System.out.print("Enter marks of subject1: ");
int one=scanner.nextInt();
System.out.print("Enter marks of subject2: ");
int two=scanner.nextInt();
System.out.print("Enter marks of subject3: ");
int three=scanner.nextInt();
Student s=new Student(num, name, one, two, three);
ss[i]=s;
System.out.println();
}
for(int i=0; i<n; i++){
System.out.println("Details of student "+(i+1)+": ");
ss[i].results();
}
}
}
class Student{
int roll;
String name;
int sub1;
int sub2;
int sub3;
Student(int r, String n, int s1, int s2, int s3){
roll=r;
name=n;
sub1=s1;
sub2=s2;
sub3=s3;
}
void results(){
System.out.println("Name of student: "+ name);
System.out.println("Roll number of student: "+ roll);
int total=sub1+sub2+sub3;
System.out.println("Total: "+total);
double perc=total/3;
System.out.println("Percentage: "+perc+" %");
char grade;
if(perc>=90){
System.out.println("Grade A");
grade='A';
}
else if(perc>=75){
System.out.println("Grade B");
grade='B';
}
else if(perc>=60){
System.out.println("Grade C");
grade='C';
}
else if(perc>=40){
System.out.println("Grade D");
grade='D';
}
else{
System.out.println("Grade F");
grade='F';
}
switch(grade){
case 'A', 'B'->System.out.println("First division");
case 'C'->System.out.println("Second division");
case 'D'->System.out.println("Third division");
case 'F'->System.out.println("Fail");
}
System.out.println();
}
}
