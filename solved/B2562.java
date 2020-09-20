import java.io.*;
public class B2562 {

	public static void main(String[] args) {
		try {
			BufferedReader input = new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output = new BufferedWriter(new OutputStreamWriter(System.out));
			int com;
			com=Integer.parseInt(input.readLine());
			int max=com;
			int count=1;
			for(int i=1;i<9;i++) {
				com=Integer.parseInt(input.readLine());
				if(max<com) {
					max=com;
					count=i+1;
				}
			}
			output.write(max+"\n"+count);
			output.flush();
			input.close();
			output.close();
		}
		catch(IOException e) {
			e.printStackTrace();
		}
	}
}
