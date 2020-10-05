import java.io.*;
public class B1929 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			String[] s=input.readLine().split(" ");
			int x=Integer.valueOf(s[0]);
			int y=Integer.valueOf(s[1]);
			int[] array=new int[1000001];
			for(int i=1;i<=y;i++) {
				if(i==1||array[i]==1)continue;
				if(array[i]==0) {
					if(x<=i&&i<=y)
						output.write(String.valueOf(i)+"\n");
					for(int i1=1;i1*i<=y;i1++) {
						if(i1*i>1000000)break;
						array[i1*i]=1;
					}
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