import java.io.*;
public class B1152 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split(" ");
			if(s.length>=1&&s[0].equals(""))
				output.write(String.valueOf(s.length-1));
			else output.write(String.valueOf(s.length));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}