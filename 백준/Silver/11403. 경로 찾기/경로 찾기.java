import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        String[][] graph = new String[N][N];
        boolean[][] answer = new boolean[N][N];
        for(int i = 0; i < N; i++){
            String[] temp = br.readLine().split(" ");
            for(int j = 0; j < N; j++){
                graph[i][j] = temp[j];
            }
        }
        for(int j = 0; j < N; j++){
            findRoute(graph, answer, N, j, j);
        }
        for(int a = 0; a< N; a++){
            for(int b = 0; b< N; b++){
                if(answer[a][b]){
                    sb.append("1");
                }else{
                    sb.append("0");
                }
                if(b != N-1){
                    sb.append(" ");
                }
                
            }sb.append("\n");
        }
        System.out.println(sb.toString());
        
    }
    public static void findRoute(String[][] graph, boolean[][] answer, int N, int current, int start){
        for(int i = 0; i < N; i++){
            if(graph[current][i].equals("1") && !answer[start][i]){
                answer[start][i] = true;
                findRoute(graph, answer, N, i, start);
            }
        }return;
    }
}