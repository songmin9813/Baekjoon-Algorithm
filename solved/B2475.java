import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class B2475 {
	
	public static void main(String[] args) {
		try {
			StringBuilder sb = new StringBuilder();
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			String[] s=input.readLine().split(" ");
			int[] nums=new int[5];
			int sum=0;
			for(int i=0;i<nums.length;i++) {
				nums[i]=Integer.parseInt(s[i]);
				sum=sum+(nums[i]*nums[i]);
			}
			sb.append(sum%10);
			System.out.print(sb);
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}