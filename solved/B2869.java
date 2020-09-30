import java.io.*;
public class B2869 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split(" ");
			int a=Integer.valueOf(s[0]);
			int b=Integer.valueOf(s[1]);
			int v=Integer.valueOf(s[2]);
			if(a>=v)output.write("1");
			else {
				v=v-a;
				output.write(String.valueOf((int)Math.ceil((double)v/(a-b))+1));;
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}