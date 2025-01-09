import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] numbers = br.readLine().split(" ");
        int N = Integer.parseInt(numbers[0]);
        int M = Integer.parseInt(numbers[1]);
        
        int[] arr = new int[M];
        boolean[] visited = new boolean[N];
        
        dfs(arr,visited, N, M, 0);
        
        
    }
    public static void dfs(int[] arr, boolean[] visited, int N, int M, int depth){
        if(depth == M){
            for(int num : arr){
                System.out.print(num + " ");
            }
            System.out.println();
            return;
        }
        
        for(int i = 0; i < N; i++ ){
            if(!visited[i]){
                arr[depth] = i + 1;
                visited[i] = true;
                dfs(arr, visited, N, M, depth + 1);
                visited[i] = false;
            }
        }
 
    }
}
