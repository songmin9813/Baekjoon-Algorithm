import java.io.*;
public class B10870 {
	public static int Fib(int n) {
		if(n==0)return 0;
		else if(n==1)return 1;
		else return Fib(n-1)+Fib(n-2);
	}
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			output.write(String.valueOf(Fib(x)));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}