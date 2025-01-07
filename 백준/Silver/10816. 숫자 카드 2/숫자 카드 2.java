import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int[] cards = new int[20000001];
        int N = Integer.parseInt(br.readLine());
        String[] numbers = br.readLine().split(" ");
        
        for(int i = 0; i < N; i++){
            int card = Integer.parseInt(numbers[i]);
            cards[card + 10000000]++;
        }
        int M = Integer.parseInt(br.readLine());
        String[] targets = br.readLine().split(" ");
        for(int j = 0; j < M; j++){
            sb.append(cards[Integer.parseInt(targets[j]) + 10000000]);
            sb.append(" ");
        }
        System.out.println(sb.toString());
        
    }
}