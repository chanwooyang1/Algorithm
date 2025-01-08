import java.util.*;
import java.io.*;
public class Main{
    static String[][] graph;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        graph = new String[N][N];
        star(N, 0, 0);
        for(int i = 0; i < N; i++){
            for(int j = 0; j < N; j++){
            	String temp = graph[i][j];
            	if(temp == null){
            		sb.append(" ");
            	}else{
            		sb.append(temp);	
            	}
                
            }
            sb.append("\n");
        }
         System.out.println(sb.toString());
        
    }
    public static void star(int size, int x, int y){
        if(size == 1){
            graph[x][y] = "*";
            return;
        }
        
        int count = 1;
        int nx = size/ 3;
        for(int i = x; i <x + size; i+= nx ){
            for(int j = y; j < y + size; j += nx){
                if(count == 5){
                	count++;
                    continue;
                }
                star(nx,i,j);
                count++;
            }
        }
        
    }
}