import java.io.*;
public class B1085 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split(" ");
			int x=Integer.valueOf(s[0]);
			int y=Integer.valueOf(s[1]);
			int w=Integer.valueOf(s[2]);
			int h=Integer.valueOf(s[3]);
			int right=w-x;
			int up=h-y;
			//x,y,up,right
			if(x<=y&&x<=up&&x<=right)
				output.write(String.valueOf(x));
			else if(y<=x&&y<=up&&y<=right)
				output.write(String.valueOf(y));
			else if(up<=x&&up<=y&&up<=right)
				output.write(String.valueOf(up));
			else output.write(String.valueOf(right));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}