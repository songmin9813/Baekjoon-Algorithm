import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
public class B1005 {
	static StringBuilder sb = new StringBuilder();
	public static void main(String[] args) {
		try {
			BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
			int repeat=Integer.parseInt(input.readLine());//�ݺ� Ƚ��
			for(int count=0;count<repeat;count++) {
				String[] s = input.readLine().split(" ");
				int vertex=Integer.parseInt(s[0]);//���
				int edge=Integer.parseInt(s[1]);//���� ����
				
				int[] inDegree=new int[vertex+1];
				
				boolean[] visited = new boolean[vertex+1];
				
				int[] constructionTime = new int[vertex+1];
				s=input.readLine().split(" ");
				for(int i=1;i<=vertex;i++)constructionTime[i]=Integer.parseInt(s[i-1]);
				//�Ǽ��ð� �迭
				
				ArrayList<ArrayList<Integer>> graph = new ArrayList<ArrayList<Integer>>();
				for(int i=0;i<vertex+1;i++) graph.add(new ArrayList<Integer>());
				//�׷��� ���� �� �ʱ�ȭ
				
				for(int i=0;i<edge;i++) {
					String[] temp2 = input.readLine().split(" ");
					int x=Integer.parseInt(temp2[0]);
					int y=Integer.parseInt(temp2[1]);
					graph.get(x).add(y);
					inDegree[y]++;
				}
				//starts�� false���� ��� start��
				int endNode=Integer.parseInt(input.readLine());
				int[] result=new int[vertex+1];
				Queue<Integer> queue = new LinkedList<Integer>();
				for(int i=1;i<=vertex;i++) {
					if(!visited[i]&&inDegree[i]==0) {
						result[i]=constructionTime[i];
						visited[i]=true;
						queue.add(i);
					}
				}//ù ����
				
				while(!queue.isEmpty()) {
					int x=queue.poll();
					for(int i1=0;i1<graph.get(x).size();i1++) {
						int index=graph.get(x).get(i1);
						result[index]=Math.max(result[index], result[x]+constructionTime[index]);
						if(--inDegree[index]==0)
							queue.add(index);
					}
				}
				System.out.println(result[endNode]);
			}
			input.close();
		}catch(IOException e) {
			e.printStackTrace();
		}
	}
}