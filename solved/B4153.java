import java.io.*;
public class B4153 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			while(true) {
				String[] s=input.readLine().split(" ");
				int x=Integer.valueOf(s[0]);
				int y=Integer.valueOf(s[1]);
				int z=Integer.valueOf(s[2]);
				if(x==0&&y==0&&z==0)break;
				if(x>y&&x>z) {
					if(y*y+z*z==x*x)
						output.write("right\n");
					else output.write("wrong\n");
				}
				else if(y>z&&y>x) {
					if(x*x+z*z==y*y)
						output.write("right\n");
					else output.write("wrong\n");
				}
				else if(z>y&&z>x) {
					if(x*x+y*y==z*z)
						output.write("right\n");
					else output.write("wrong\n");
				}
				else output.write("wrong\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}