import java.io.*;
public class B2675 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String[] s;
			for(int i=0;i<x;i++) {
				s=input.readLine().split(" ");
				for(int i1=0;i1<s[1].length();i1++) {
					for(int i2=0;i2<Integer.valueOf(s[0]);i2++)
						output.write(s[1].charAt(i1));
				}
				output.write("\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}