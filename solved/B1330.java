import java.util.Scanner;
public class B1330 {

	public static void main(String[] args) {
		int x, y;
		Scanner input = new Scanner(System.in);
		x=input.nextInt();
		y=input.nextInt();
		if(x>y) System.out.println(">");
		else if(x<y) System.out.println("<");
		else System.out.println("==");
	}

}
