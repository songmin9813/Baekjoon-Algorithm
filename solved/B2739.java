import java.util.Scanner;
public class B2739 {

	public static void main(String[] args) {
		int x;
		Scanner input = new Scanner(System.in);
		x=input.nextInt();
		for(int i=1;i<=9;i++)
			System.out.println(x+" * "+i+" = "+x*i);
		input.close();
	}
}