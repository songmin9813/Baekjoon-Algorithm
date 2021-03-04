import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
public class B2920 {
	
	public static void main(String[] args) {
		try {
			StringBuilder sb = new StringBuilder();
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			String[] s=input.readLine().split(" ");
			int[] nums=new int[8];
			for(int i=0;i<8;i++) nums[i]=Integer.parseInt(s[i]);
			if(nums[0]==1&&nums[1]==2&&nums[2]==3&&nums[3]==4&&nums[4]==5&&nums[5]==6&&nums[6]==7&&nums[7]==8)
				sb.append("ascending");
			else if(nums[0]==8&&nums[1]==7&&nums[2]==6&&nums[3]==5&&nums[4]==4&&nums[5]==3&&nums[6]==2&&nums[7]==1)
				sb.append("descending");
			else sb.append("mixed");
			System.out.print(sb);
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}