import java.io.*;
public class B2908 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s = input.readLine().split(" ");
			int x = Integer.valueOf(s[0]);
			int y = Integer.valueOf(s[1]);
			x = (x%10)*100+(x/10%10)*10+(x/100);
			y = (y%10)*100+(y/10%10)*10+(y/100);
			if(x>y)output.write(String.valueOf(x));
			else output.write(String.valueOf(y));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}