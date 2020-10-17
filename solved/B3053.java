import java.io.*;
public class B3053 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			double uclid=x*x*Math.PI;
			double taxi=2*x*x;
			output.write(String.valueOf(uclid)+"\n"+String.valueOf(taxi));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}