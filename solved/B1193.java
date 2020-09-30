import java.io.*;
public class B1193 {
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int x=Integer.parseInt(input.readLine());
			int left=1,right=1,right_up=1;
			int i;
			for(i=1;i!=x;i++) {
				if(right_up==1) {
					if(left==1) {
						right+=1;
						right_up=0;
					}
					else {
						left--;
						right++;
					}
				}
				else {
					if(right==1) {
						left+=1;
						right_up=1;
					}
					else {
						left++;
						right--;
					}
				}
			}
			output.write(String.valueOf(left+"/"+right));
			output.flush();
			output.close();
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}