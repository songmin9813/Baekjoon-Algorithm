import java.util.Scanner;
public class B10871 {
	public static void main(String[] args) {
		int n,x,tmp;
		Scanner input = new Scanner(System.in);
		n=input.nextInt();
		x=input.nextInt();
		for(int i=0;i<n;i++) {
			tmp=input.nextInt();
			if(tmp<x) System.out.print(tmp+" ");
		}
	}
}