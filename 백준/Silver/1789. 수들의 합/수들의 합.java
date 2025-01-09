import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long S = Long.parseLong(br.readLine());
        long answer = 0;
        long count = 0;
        while(true){
        
            answer += count;
            	
            if(answer > S){
            	break;
            }
            count++;
        }
     System.out.println(count - 1);   
    }
}