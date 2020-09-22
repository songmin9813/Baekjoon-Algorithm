import java.util.Scanner;
public class B8393 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int x;
		int sum=0;
		x=input.nextInt();
		for(int i=1;i<=x;i++)
			sum+=i;
		System.out.print(sum);
		input.close();
	}
}