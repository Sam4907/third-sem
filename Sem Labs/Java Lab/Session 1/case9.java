//A college requires 75% attendance to sit for exams. 
//Read total classes held and classes attended for N students (loop), calculate percentage for each, and print "Eligible" or "Not Eligible" (if-else) along with shortage percentage if not eligible. 

import java.util.Scanner;

public class case9{
    public static void main(String[] args){
        Scanner scanner=new Scanner(System.in);

        System.out.print("Enter the number of students: ");
        int n=scanner.nextInt();

        for (int i=1; i<=n; i++) {
            System.out.println("\nStudent " + i + "");
            
            System.out.print("Enter total classes held: ");
            int totalClasses=scanner.nextInt();
            
            System.out.print("Enter classes attended: ");
            int classesAttended=scanner.nextInt();

            if (totalClasses<=0) {
                System.out.println("Invalid input: Total classes must be greater than 0.");
                continue;
            }

            double attendancePercentage=((double) classesAttended / totalClasses) * 100;
            System.out.printf("Attendance: %.2f%%\n", attendancePercentage);

            if (attendancePercentage>=75.0) {
                System.out.println("Status: Eligible");
            } else {
                System.out.println("Status: Not Eligible");
                double shortage=75.0-attendancePercentage;
                System.out.printf("Shortage: %.2f%%\n", shortage);
            }
        }

        scanner.close();
    }
}