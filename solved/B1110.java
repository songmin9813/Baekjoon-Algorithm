import java.io.*;
public class B1110 {
	public static void main(String[] args) {
		try {
			int count=0;
			int a=0,b,tmp;
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			tmp=x;
			while(true) {
				b=tmp%10;
				a=tmp/10;
				tmp=(b*10)+((a+b)%10);
				count++;
				if(tmp==x)break;
			}
			output.write(String.valueOf(count));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}