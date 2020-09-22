import java.util.Scanner;
public class B10950 {
	public static void main(String[] args) {
		Scanner input=new Scanner(System.in);
		int x,y,z;
		x=input.nextInt();
		for(int i=0;i<x;i++) {
			y=input.nextInt();
			z=input.nextInt();
			System.out.println(y+z);
		}
		input.close();
	}
}