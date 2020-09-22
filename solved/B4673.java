import java.io.*;
public class B4673 {
	public static void main(String[] args) {
		try {
			BufferedWriter output=new BufferedWriter(new OutputStreamWriter(System.out));
			int[] array = new int[10000];
			int temp=0;
			for(int i=0;i<array.length;i++) {
				if(array[i]==1)continue;
				else output.write(String.valueOf((i+1)+"\n"));
				for(int i1=i;;) {
					temp=getSelf(i1+1);
					if(temp>10000) break;
					array[temp-1]=1;
					i1=temp-1;
				}
			}
			output.flush();
			output.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
	static int getDigit(int a) {
		int result=0;
		while(true) {
			a/=10;
			result++;
			if(a==0)break;
		}
		return result;
	}
	static int getSelf(int a) {
		int result=a;
		int a1=a;
		for(int i=0;i<getDigit(a);i++) {
			result=result+(a1%10);
			a1/=10;
		}
		return result;
	}
}