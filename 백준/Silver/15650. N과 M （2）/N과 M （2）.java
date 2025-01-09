import java.util.*;
import java.io.*;
public class Main{ 
    public static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] answer = new int[M];
        boolean[] visited = new boolean[N + 1];
        
        dfs(N, M, 0, answer, visited);
        System.out.println(sb.toString());
    }
    
    public static void dfs(int N, int M, int depth, int[] answer, boolean[] visited){
        if(depth == M){
            for(int num : answer){
                sb.append(num).append(" ");
            }
            sb.append("\n");
            return;
        }
        
        for(int i = 1; i <= N; i++){
            if(!visited[i] && (depth == 0 || i > answer[depth - 1])){
            	
                visited[i] = true;
                answer[depth] = i; 
                dfs(N, M, depth + 1, answer, visited);
                visited[i] = false;
            }
        }
        
        
    }
}