import java.io.*;
public class B11022 {
	public static void main(String[] args) {
		int sum, a, b;
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			
			for(int i=0;i<x;i++) {
				String s=input.readLine();
				String[] array=s.split(" ");
				a=Integer.parseInt(array[0]);
				b=Integer.parseInt(array[1]);
				sum=a+b;
				output.write("Case #"+(i+1)+": "+a+" + "+b+" = "+String.valueOf(sum+"\n"));
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}