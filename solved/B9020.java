import java.io.*;
public class Main {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			int[] array=new int[10001];
			for(int i=1;i<=10000;i++) {
				if(i==1||array[i]==1)continue;
				if(array[i]==0) {
					for(int i1=2;i1*i<=10001;i1++) {
						if(i1*i>10000)break;
						array[i1*i]=1;
					}
				}
			}
			for(int i=0;i<x;i++) {
				int y=Integer.parseInt(input.readLine());
				int half=y/2;
				for(int i1=half;i1>0;i1--) {
					if(array[i1]==0&&array[y-i1]==0){
					    half=i1; break;
					}
				}
				output.write(String.valueOf(half)+" "+String.valueOf(y-half)+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}