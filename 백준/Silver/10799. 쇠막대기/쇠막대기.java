import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int left = 0;
        int answer = 0;
        String input = br.readLine();
        for(int i = 0; i< input.length(); i++){
            if(input.charAt(i) == '('){
                left++;
            }else{
                if(input.charAt(i-1) == '('){
                  left--;
                    answer += left;  
                }else{
                    
                    left--;
                    answer += 1;
                }
                
            }
        }
        System.out.println(answer);
    }
}