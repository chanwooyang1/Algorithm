import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int T = Integer.parseInt(br.readLine());
        
        for(int i = 0;i < T; i++){
            int N = Integer.parseInt(br.readLine());
            int[] woods = new int[N];
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < N; j++){
                woods[j] = Integer.parseInt(st.nextToken());
            }
            System.out.println(findMinDiff(sortWoods(woods)));
            
        }
        
    }
    public static int[] sortWoods(int[] arr){
        int length = arr.length;
        
        int[] sorted = new int[length];
        Arrays.sort(arr);
        int index = 0;
        if(length % 2 == 0){
            for(int i = 0; i < length; i+= 2){
                sorted[index] = arr[i];
                sorted[length - index - 1] = arr[i + 1];
                index++;
            }
        }else{
            for(int j = 0; j < length - 1; j+= 2){
            	
            	sorted[index] = arr[j];
                sorted[length - index - 1] = arr[j + 1];
                index++;
            }
            sorted[(length/2)] = arr[length - 1];
        }
       
        return sorted;
    }
    
    public static int findMinDiff(int[] arr){
        int length = arr.length;
        int minDiff = Integer.MIN_VALUE;
        for(int i = 0; i < length; i++){
            if(i == length - 1){
                minDiff = Math.max(minDiff, Math.abs(arr[i] - arr[0]));
            }else{
            	minDiff = Math.max(minDiff, Math.abs(arr[i] - arr[i + 1]));	
            }
            
        }
        return minDiff;
    }
}