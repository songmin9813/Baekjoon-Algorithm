import java.io.*;
public class B1011 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int t=Integer.parseInt(input.readLine());
			int x,count,sum;
			for(int i=0;i<t;i++) {
				String[] s=input.readLine().split(" ");
				x=Integer.valueOf(s[1])-Integer.valueOf(s[0]);
				if(x==1) {
					output.write("1\n");break;
				}
				count=1;
				sum=0;
				while(true) {
					sum+=count;
					if(sum*2-count<=x&&x<sum*2+count+1) {
						if(sum*2==x)output.write(String.valueOf(count*2)+"\n");
						else output.write(String.valueOf(count*2+1)+"\n");
						break;
					}
					count++;
				}
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}