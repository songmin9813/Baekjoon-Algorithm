import java.io.*;
public class B2839 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			int result;
			if(x==4||x==7) result=-1;
			else if(x%10==0||x%10==5) result=x/5;
			else if(x%10==1||x%10==6) {
				x-=6;
				result=x/5+2;
			}
			else if(x%10==2)
			{
				x-=12;
				result=x/5+4;
			}
			else if(x%10==3||x%10==8) {
				x-=3;
				result=x/5+1;
			}
			else if(x%10==4||x%10==9) {
				x-=9;
				result=x/5+3;
			}
			else{//x%10==7
				x-=12;
				result=x/5+4;
			}
			output.write(String.valueOf(result));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}