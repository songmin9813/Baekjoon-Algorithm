import java.util.Scanner;
public class B2753 {

	public static void main(String[] args) {
		int x;
		Scanner input = new Scanner(System.in);
		x=input.nextInt();
		if(((x%4==0)&&(x%100!=0))||x%400==0)
			System.out.println("1");
		else System.out.println("0");
	}
}