import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int count1 = 0;
        
        
        String input = br.readLine();
        int length = input.length();
        for(int i = 0; i < length - 1; i++){
            char current = input.charAt(i);
            char next = input.charAt(i+1);
            
            if(current != next){
                count1++;
            }
            
        }
        
        
        System.out.println((count1 + 1) / 2);
    }
}
