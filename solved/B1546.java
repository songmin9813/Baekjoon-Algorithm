import java.io.*;
public class B1546 {
	public static void main(String[] args) {
		float max,avg;
		float sum=0;
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String[] array=input.readLine().split(" ");
			float[] array2=new float[x];
			for(int i=0;i<x;i++)
				array2[i]=Float.valueOf(array[i]);
			max=array2[0];
			for(int i=1;i<x;i++)
				if(max<array2[i])
					max=array2[i];
			for(int i=0;i<x;i++) {
				array2[i]=array2[i]/max*100;
				sum+=array2[i];
			}
			output.write(String.valueOf(sum/x));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}