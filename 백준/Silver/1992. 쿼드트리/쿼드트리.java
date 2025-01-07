import java.util.*;
import java.io.*;
public class Main{
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        String[][] arr = new String[N][N];
        for(int i = 0; i < N; i++){
            String[] temp = br.readLine().split("");
            for(int j = 0; j < N; j++){
                arr[i][j] = temp[j];
            }
        }
        
        
        
        quadzip(arr, 0, 0, N);
        
        System.out.println(sb.toString());
        
    }
    
    public static void quadzip(String[][] arr, int x, int y, int length){
        if(check(arr, x, y, length, arr[x][y])){
            sb.append(arr[x][y]);
            return;
        }
        sb.append("(");
        quadzip(arr, x, y, length/2);
        
        quadzip(arr, x, y + length/2, length/2);
        quadzip(arr, x + length /2 , y, length/2);
        quadzip(arr, x + length/2 , y + length/2, length/2);
        sb.append(")");
    }
    public static boolean check(String[][] arr, int x, int y, int length, String arrVal){
        for(int i = x; i < x + length; i++){
            for(int j = y; j< y + length; j++){
                if(!arr[i][j].equals(arrVal)){
                    return false;
                }
            }
        }return true;
    }
}