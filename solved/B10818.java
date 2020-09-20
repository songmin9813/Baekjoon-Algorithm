import java.io.*;
public class B10818 {
	public static void main(String[] args) {
		try {
			int min,max;
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String s = input.readLine();
			String[] array = s.split(" ");
			min=Integer.parseInt(array[0]);
			max=Integer.parseInt(array[0]);
			for(int i=0;i<x;i++) {
				if(min>Integer.parseInt(array[i]))
					min=Integer.parseInt(array[i]);
				if(max<Integer.parseInt(array[i]))
					max=Integer.parseInt(array[i]);
			}
			output.write(min+" "+max);
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}