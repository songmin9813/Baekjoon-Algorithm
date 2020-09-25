import java.io.*;
public class B1157 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String s=input.readLine();
			int[] array=new int[26];
			int count=0;
			for(int i=0;i<s.length();i++) {
				if((int)s.charAt(i)>=65&&(int)s.charAt(i)<=90)
					array[(int)s.charAt(i)-65]++;
				else array[(int)s.charAt(i)-97]++;
			}
			int max=0;
			for(int i=1;i<array.length;i++)
				if(array[max]<array[i])max=i;
			for(int i=0;i<array.length;i++)
				if(array[max]==array[i])count++;
			if(count>=2)output.write("?");
			else output.write(String.valueOf((char)(max+65)));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}