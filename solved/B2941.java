import java.io.*;
public class B2941 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String s = input.readLine();
			int count=0;
			for(int i=0;i<s.length();i++) {
				if(i<=s.length()-3&&s.charAt(i)=='d') {
					if(s.charAt(i+1)=='z'&&s.charAt(i+2)=='=') {
						count++; i+=2; continue;
					}
				}
				if(i<=s.length()-2&&s.charAt(i)=='d') {
					if(s.charAt(i+1)=='-') {
						count++; i++; continue;
					}
				}
				else if(i<=s.length()-2&&s.charAt(i)=='c') {
					if(s.charAt(i+1)=='=') {
						count++; i++; continue;
					}
					else if(s.charAt(i+1)=='-') {
						count++; i++; continue;
					}
				}
				else if(i<=s.length()-2&&s.charAt(i)=='l') {
					if(s.charAt(i+1)=='j') {
						count++; i++; continue;
					}
				}
				else if(i<=s.length()-2&&s.charAt(i)=='n') {
					if(s.charAt(i+1)=='j') {
						count++; i++; continue;
					}
				}
				else if(i<=s.length()-2&&s.charAt(i)=='s') {
					if(s.charAt(i+1)=='=') {
						count++; i++; continue;
					}
				}
				else if(i<=s.length()-2&&s.charAt(i)=='z') {
					if(s.charAt(i+1)=='=') {
						count++; i++; continue;
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