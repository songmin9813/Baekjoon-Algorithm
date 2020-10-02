import java.io.*;
public class B10809 {
	public static void main(String[] args) {
		try {//-97
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split("");
			int[] al=new int[26];
			for(int i=0;i<al.length;i++) al[i]=-1;
			for(int i=0;i<s.length;i++) {
				if(al[Integer.valueOf((int)(s[i].charAt(0)))-97]!=-1)
					continue;
				al[Integer.valueOf((int)(s[i].charAt(0)))-97]=i;
			}
			for(int i=0;i<al.length;i++)
				output.write(String.valueOf(al[i])+" ");
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}