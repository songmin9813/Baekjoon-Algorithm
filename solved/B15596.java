import java.io.*;
public class B15596 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s = input.readLine().split(" ");
			int[] array = new int[s.length];
			for(int i=0;i<s.length;i++)
				array[i]=Integer.valueOf(s[i]);
			output.write(String.valueOf(sum(array)));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
	//use code below if you want to pass
	static long sum(int[] a) {
		long result=0;
		for(int i=0;i<a.length;i++)
			result+=a[i];
		return result;
	}
}