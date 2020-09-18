import java.io.*;
public class B15552 {
	public static void main(String[] args) {
		int sum;
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			
			for(int i=0;i<x;i++) {
				String s=input.readLine();
				String[] array=s.split(" ");
				sum=0;
				for(int i1=0;i1<array.length;i1++)
					sum+=Integer.parseInt(array[i1]);
				output.write(String.valueOf(sum+"\n"));
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}