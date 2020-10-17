import java.io.*;
public class B1002 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			for(int i=0;i<x;i++) {
				String[] s=input.readLine().split(" ");
				int x1=Integer.valueOf(s[0]);
				int y1=Integer.valueOf(s[1]);
				int r1=Integer.valueOf(s[2]);
				int x2=Integer.valueOf(s[3]);
				int y2=Integer.valueOf(s[4]);
				int r2=Integer.valueOf(s[5]);
				double distance=Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
				int result;
				if(distance==0) {
					if(r1==r2)result=-1;
					else result=0;
				}
				else if(r1+r2<distance) result=0;
				else if(r1+r2==distance) result=1;
				else if(r1<=r2&&r1+r2>distance&&distance+r1>r2) result=2;
				else if(r1>r2&&r1+r2>distance&&distance+r2>r1) result=2;
				else if(r1>r2&&distance+r2==r1)result=1;
				else if(r1<r2&&distance+r1==r2)result=1;
				else result=0;
				output.write(String.valueOf(result)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}