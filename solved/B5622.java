import java.io.*;
public class B5622 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String s = input.readLine();
			int sum=0;
			for(int i=0;i<s.length();i++) {
				if(s.charAt(i)=='A'||s.charAt(i)=='B'||s.charAt(i)=='C')
					sum+=3;
				else if(s.charAt(i)=='D'||s.charAt(i)=='E'||s.charAt(i)=='F')
					sum+=4;
				else if(s.charAt(i)=='G'||s.charAt(i)=='H'||s.charAt(i)=='I')
					sum+=5;
				else if(s.charAt(i)=='J'||s.charAt(i)=='K'||s.charAt(i)=='L')
					sum+=6;
				else if(s.charAt(i)=='M'||s.charAt(i)=='N'||s.charAt(i)=='O')
					sum+=7;
				else if(s.charAt(i)=='P'||s.charAt(i)=='Q'||s.charAt(i)=='R'||s.charAt(i)=='S')
					sum+=8;
				else if(s.charAt(i)=='T'||s.charAt(i)=='U'||s.charAt(i)=='V')
					sum+=9;
				else if(s.charAt(i)=='W'||s.charAt(i)=='X'||s.charAt(i)=='Y'||s.charAt(i)=='Z')
					sum+=10;
			}
			output.write(String.valueOf(sum));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}