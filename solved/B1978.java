import java.io.*;
public class B1978 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			String[] s=input.readLine().split(" ");
			int com;
			int count=0;
			for(int i=0;i<x;i++) {
				com=Integer.valueOf(s[i]);
				for(int i1=1;i1<=com;i1++){
				    if(com==1){
				        count--;
				        break;
				    }
				    if(i1==1||i1==com)continue;
				    if(com%i1==0){
				        count--;
				        break;
			    	}
			    }
			    count++;
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