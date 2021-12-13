import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
public class taewoo_samsung2 {
   static boolean judge(String a, String b, String c) {
      boolean flag=true;
      for(int i=0;i<4;i++) {
         if(!((a.charAt(i)==b.charAt(i)&&b.charAt(i)==c.charAt(i)&&a.charAt(i)==c.charAt(i))||
            (a.charAt(i)!=b.charAt(i)&&b.charAt(i)!=c.charAt(i)&&a.charAt(i)!=c.charAt(i)))) {
            flag=false;
            break;
         }
      }
      return flag;
   }
   static void backtracking(ArrayList<ArrayList<Integer[]>> graph, boolean[] visited, int count, int index) {
      for(int i=index;i<graph.size();i++) {
         if(visited[i]==false) {
            visited[i]=true;
            for(int i1=0;i1<graph.get(i).size();i1++) {
               int a=graph.get(i).get(i1)[0];
               int b=graph.get(i).get(i1)[1];
               if(visited[a]==false&&visited[b]==false) {
                  visited[a]=true;
                  visited[b]=true;
                  backtracking(graph, visited, count+1, i);
                  visited[a]=false;
                  visited[b]=false;
               }
            }
            visited[i]=false;
         }
      }
      if(result<count)
         result=count;
   }
   static int result=0;
   
   static StringBuilder sb=new StringBuilder();
   public static void main(String[] args) throws IOException{
      
      BufferedReader input=new BufferedReader(new InputStreamReader(System.in));
      StringBuilder sb=new StringBuilder();
      int tc=Integer.parseInt(input.readLine());
      for(int i=0;i<tc;i++) {
         ArrayList<ArrayList<Integer[]>> graph=new ArrayList<ArrayList<Integer[]>>();
         int n=Integer.parseInt(input.readLine());
         String[] cards=new String[n];
         for(int i1=0;i1<n;i1++) {
            graph.add(new ArrayList<Integer[]>());
            cards[i1]=input.readLine();
         }//ÀÔ·Â¿Ï·á
         for(int one=0;one<n-2;one++) {
            for(int two=one+1;two<n-1;two++) {
               for(int thr=two+1;thr<n;thr++) {
                  if(judge(cards[one],cards[two],cards[thr])) {
                     graph.get(one).add(new Integer[] {two, thr});
                  }
               }
            }
         }//Â¦²áµéÀÌ ¸¸µé¾îÁü
         boolean[] visited=new boolean[n];
         result=0;
         backtracking(graph, visited, 0, 0);
         sb.append('#'+String.valueOf(i+1)+' '+String.valueOf(result)+'\n');
      }
      System.out.print(sb);
      input.close();
   }
}