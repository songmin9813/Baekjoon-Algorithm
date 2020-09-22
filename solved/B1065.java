import java.io.*;
public class B1065 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			int count=0;
			if(x<100) output.write(String.valueOf(x));
			else if(x==1000) output.write("144");
			else {
				for(int i=100;i<=x;i++)
					if((i/100)-(i/10%10)==(i/10%10)-(i%10))
						count++;
				output.write(String.valueOf(count+99));
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}