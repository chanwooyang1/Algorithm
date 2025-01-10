import java.util.*;
import java.io.*;
public class Main{
    public static int N;
    public static int answer = 0;
    public static boolean[] columns, diag1, diag2;
 
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        int depth = 0;
        columns = new boolean[N];          // 열 충돌 체크
        diag1 = new boolean[2 * N];        // 오른쪽 아래 대각선
        diag2 = new boolean[2 * N];  
        
        dfs(depth);
        System.out.println(answer);
        
       
        
        
    }
    public static void dfs(int depth){
        if(depth == N){
            answer++;
            return;
            
        }
        
        for (int i = 0; i < N; i++) {
            if (!columns[i] && !diag1[depth - i + N] && !diag2[depth + i]) {
                columns[i] = true;
                diag1[depth - i + N] = true;
                diag2[depth + i] = true;
                
                dfs(depth + 1); // 다음 행으로 이동
                
                // 백트래킹: 상태 복원
                columns[i] = false;
                diag1[depth - i + N] = false;
                diag2[depth + i] = false;
            }
        }
    }
}