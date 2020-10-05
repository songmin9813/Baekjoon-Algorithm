import java.io.*;
public class B4948 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int[] array=new int[246913];
			int x,count;
			while(true) {
				count=0;
				x=Integer.parseInt(input.readLine());
				if(x==0) break;
				for(int i=1;i<=2*x;i++) {
					if(i==1||array[i]==1)continue;
					if(array[i]==0) {
						if(x<i&&i<=2*x) count++;
						for(int i1=2;i1*i<=2*x;i1++) {
							if(i1*i>2*x) break;
							array[i1*i]=1;
						}
					}
				}
				output.write(String.valueOf(count)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}