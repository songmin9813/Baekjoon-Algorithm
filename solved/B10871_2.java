import java.io.*;
public class B10871_2 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String array[];
			String s=input.readLine();
			array = s.split(" ");
			int n=Integer.valueOf(array[0]);
			int x=Integer.valueOf(array[1]);
			s=input.readLine();
			array = s.split(" ");
			for(int i=0;i<n;i++)
				if(x>Integer.valueOf(array[i]))
					output.write(array[i]+" ");
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}