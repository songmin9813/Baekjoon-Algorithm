import java.io.*;
public class B2775 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			int k,n;
			for(int i=0;i<x;i++) {
				k=Integer.parseInt(input.readLine());
				n=Integer.parseInt(input.readLine());
				int[] a=new int[n];
				for(int i1=0;i1<a.length;i1++)
					a[i1]=i1+1;
				for(int i2=0;i2<k;i2++) {
					for(int i1=0;i1<n;i1++) {
						if(i1==0)continue;
						a[i1]+=a[i1-1];
					}
				}
				output.write(String.valueOf(a[a.length-1])+"\n");
			}
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}