import java.io.*;
public class B2577 {
	public static void main(String[] args) {
		try {
			int[] array = new int[10];
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int result
			=Integer.parseInt(input.readLine())
			*Integer.parseInt(input.readLine())
			*Integer.parseInt(input.readLine());
			while(true) {
				array[result%10]+=1;
				result/=10;
				if(result==0) break;
			}
			for(int i=0;i<10;i++)
				output.write(array[i]+"\n");
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}