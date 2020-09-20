import java.io.*;
public class B3052 {
	public static void main(String[] args) {
		try {
			int[] array = new int[10];
			int count=10;
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			for(int i=0;i<10;i++) {
				array[i]=Integer.parseInt(input.readLine())%42;
			}
			for(int i=0;i<array.length-1;i++) {
				if(array[i]==-1)continue;
				for(int i1=i+1;i1<array.length;i1++) {
					if(array[i1]==-1) continue;
					if(array[i]==array[i1]) {
						count--;
						array[i1]=-1;
					}
				}
			}
			output.write(String.valueOf(count));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}