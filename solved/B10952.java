import java.io.*;
public class B10952 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String array[],s;
			int x,y;
			while(true) {
				s=input.readLine();
				array = s.split(" ");
				x=Integer.valueOf(array[0]);
				y=Integer.valueOf(array[1]);
				if(x==0&&y==0)break;
				output.write((x+y)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}