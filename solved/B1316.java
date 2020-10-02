import java.io.*;
public class B1316 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String s;
			int count=0;
			for(int i=0;i<x;i++) {
				int[] array=new int[26];
				s=input.readLine();
				for(int i1=0;i1<s.length();i1++) {
					if(array[(int)s.charAt(i1)-97]==-1) {
						count--; break;
					}
					if(i1==0)array[(int)s.charAt(i1)-97]++;
					else {
						if(array[(int)s.charAt(i1-1)-97]!=array[(int)s.charAt(i1)-97])
							array[(int)s.charAt(i1-1)-97]=-1;
						array[(int)s.charAt(i1)-97]++;
					}
				}
				count++;
			}
			output.write(String.valueOf(count));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}