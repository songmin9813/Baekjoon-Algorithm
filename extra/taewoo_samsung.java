import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class taewoo_samsung {
	static StringBuilder sb=new StringBuilder();
	public static void main(String[] args) throws IOException{
		BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb=new StringBuilder();
		int tc=Integer.parseInt(input.readLine());
		for(int i=0;i<tc;i++) {
			int result=0;
			int n=Integer.parseInt(input.readLine());
			int[] list_=new int[n];
			StringTokenizer stk = new StringTokenizer(input.readLine());
			for(int i1=0;i1<n;i1++)
				list_[i1]=Integer.parseInt(stk.nextToken());
			Arrays.sort(list_);
			Deque<Integer> oddlist=new LinkedList<Integer>();
			Deque<Integer> evenlist=new LinkedList<Integer>();
			for(int i1=0;i1<n;i1++) {
				if(list_[i1]%2==0) evenlist.add(list_[i1]);
				else oddlist.add(list_[i1]);
			}
			while(oddlist.size()!=1&&oddlist.size()!=0) {
				result+=oddlist.pollLast();
				oddlist.pollFirst();
			}
			while(evenlist.size()!=1&&evenlist.size()!=0) {
				result+=evenlist.pollLast();
				evenlist.pollFirst();
			}
			if(oddlist.size()==1)
				result+=Math.min(evenlist.pop(), oddlist.pop());
			sb.append('#'+String.valueOf(i+1)+' '+String.valueOf(result)+'\n');
		}
		System.out.print(sb);
		input.close();
	}
}