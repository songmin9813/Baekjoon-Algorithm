import java.io.*;
public class B1712_2 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split(" ");
			int a=Integer.valueOf(s[0]);
			int b=Integer.valueOf(s[1]);
			int c=Integer.valueOf(s[2]);
			long result;
			if(c<=b)result=-1;
			else result=(long) (a/(c-b)+1);
			output.write(String.valueOf(result));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}