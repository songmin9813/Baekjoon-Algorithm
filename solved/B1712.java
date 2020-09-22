import java.util.Scanner;
public class B1712 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int a=input.nextInt();
		int b=input.nextInt();
		int c=input.nextInt();
		long result;
		if(c<=b)result=-1;
		else result=(long)(a/(c-b)+1);
		System.out.print(result);
		input.close();
	}
}