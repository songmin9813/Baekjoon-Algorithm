import java.io.*;
public class B10872 {
	public static int Fac(int n) {
		if(n==1||n==0)return 1;
		else return n*Fac(n-1);
	}
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			output.write(String.valueOf(Fac(x)));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}