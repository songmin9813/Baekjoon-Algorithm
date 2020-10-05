import java.io.*;
public class B2581 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			int y=Integer.parseInt(input.readLine());
			int temp;
			int sum=0,min=10000;
			int count;
			if(x==1)x++;
			for(;x<=y;x++) {
				count=0;
				temp=(int)Math.floor(Math.sqrt((double)x));
				for(int i1=1;i1<=temp;i1++)
					if(x%i1==0)count++;
				if(count==1) {
					sum+=x;
					if(min>x)min=x;
				}
			}
			if(sum==0)
				output.write("-1");
			else
				output.write(String.valueOf(sum)+"\n"+String.valueOf(min));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}