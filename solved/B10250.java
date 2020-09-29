import java.io.*;
public class B10250 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String[] s;
			int h,w,n;
			for(int i=0;i<x;i++) {
				s=input.readLine().split(" ");
				h=Integer.valueOf(s[0]);
				w=Integer.valueOf(s[1]);
				n=Integer.valueOf(s[2]);
				if(n%h==0)
					output.write(String.valueOf(h)+String.format("%02d", n/h)+"\n");
				else
					output.write(String.valueOf(n%h)+String.format("%02d", n/h+1)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}