import java.io.*;
public class B3009 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split(" ");
			int x1=Integer.valueOf(s[0]);
			int y1=Integer.valueOf(s[1]);
			s=input.readLine().split(" ");
			int x2=Integer.valueOf(s[0]);
			int y2=Integer.valueOf(s[1]);
			s=input.readLine().split(" ");
			int x3=Integer.valueOf(s[0]);
			int y3=Integer.valueOf(s[1]);
			int x,y;
			if(x1==x2) x=x3;
			else if(x1==x3) x=x2;
			else x=x1;
			if(y1==y2) y=y3;
			else if(y1==y3) y=y2;
			else y=y1;
			output.write(String.valueOf(x+" "+y));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}