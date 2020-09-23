import java.io.*;
public class B2292 {
	public static void main(String[] args) {
		try {
			int count=1;
			int right=1;
			int left;
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			if(x==1)output.write("1");
			else {
				while(true) {
					left=right+1;
					right=left+(6*count-1);	
					if(left<=x&&x<=right)break;
					else count++;
				}
				output.write(String.valueOf(count+1));
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}