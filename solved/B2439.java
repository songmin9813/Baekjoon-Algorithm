import java.io.*;
public class B2439 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			for(int i=1;i<=x;i++) {
				for(int i2=1;i2<=x-i;i2++) output.write(" ");
				for(int i1=1;i1<=i;i1++) output.write("*");
				output.write("\n");
			}
			output.flush();
			input.close();
			output.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}