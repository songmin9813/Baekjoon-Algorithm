import java.util.Scanner;
public class B2588 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int x;
		int y;
		x=input.nextInt();
		y=input.nextInt();
		int sum=x*y;
		System.out.println(x*(y%10));
		y/=10;
		System.out.println(x*(y%10));
		y/=10;
		System.out.println(x*(y%10));
		System.out.println(sum);
		input.close();
	}
}