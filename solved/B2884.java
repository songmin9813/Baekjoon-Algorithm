import java.util.Scanner;
public class B2884 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		int x, y;
		x=input.nextInt();
		y=input.nextInt();
		if(y<45) {
			y=60-Math.abs(y-45);
			if(x==0) x=23;
			else x-=1;
		}
		else y-=45;
		System.out.println(x+" "+y);
		input.close();
	}
}