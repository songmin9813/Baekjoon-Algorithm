import java.io.*;
public class B4344 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String[] s;
			//String s1;
			float sum;
			int count;
			for(int i=0;i<x;i++) {
				sum=0;
				count=0;
				s=input.readLine().split(" ");
				for(int i1=1;i1<Integer.valueOf(s[0])+1;i1++)
					sum+=Integer.valueOf(s[i1]);
				for(int i1=1;i1<Integer.valueOf(s[0])+1;i1++)
					if(sum/Integer.valueOf(s[0])<Integer.valueOf(s[i1])) count++;
				//s1=String.format("%.2f", s);
				output.write(String.format("%.3f",count/Float.valueOf(s[0])*100)+"%\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}