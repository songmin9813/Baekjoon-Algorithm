import java.io.*;
public class B8958 {
	public static void main(String[] args) {
		int count, sum;
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String[] array;
			for(int i=0;i<x;i++) {
				sum=0;
				count=0;
				array=input.readLine().split("");
				for(int i1=0;i1<array.length;i1++) {
					if(array[i1].equals("O")) {
						count++;
						sum+=count;
					}
					else count=0;
				}
				output.write(String.valueOf(sum)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}