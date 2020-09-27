import java.io.*;
public class B1011 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int t=Integer.parseInt(input.readLine());
			String[] s;
			int x,left,right=1;
			for(int i=0;i<t;i++) {
				s=input.readLine().split(" ");
				x=Integer.valueOf(s[1])-Integer.valueOf(s[0]);
				int temp=(int)(Math.sqrt((double)x)+0.5);
				if(temp*temp==x) {
					output.write(String.valueOf(temp*2-1)+"\n");continue;
				}
				left=(int)(Math.sqrt((double)x));
				right=left+1;
				if(left*left<x&&x<=((right*right)-(left*left))/2+(left*left))
					output.write(String.valueOf(2*left)+"\n");
				else output.write(String.valueOf(2*left+1)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}