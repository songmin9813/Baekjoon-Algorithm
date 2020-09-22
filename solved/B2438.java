import java.io.*;
public class B2438 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			for(int i=1;i<=x;i++) {
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