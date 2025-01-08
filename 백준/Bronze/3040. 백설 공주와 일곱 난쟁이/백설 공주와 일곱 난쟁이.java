import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        StringBuilder sb = new StringBuilder();
        int[] dwarfs = new int[9];
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        for(int i = 0; i< 9; i++){
            dwarfs[i] = sc.nextInt();
            sum += dwarfs[i];
        }
        int del1 = 11;
        int del2 = 11;
        for(int a = 0; a < 9; a++){
            for(int b = a + 1; b < 9; b++){
                if (sum - (dwarfs[a] + dwarfs[b]) == 100){
                    del1 = a;
                    del2 = b;
                    break;
                }
            }
            if(del1 != 11){
                break;
            }
        }
        for(int k = 0; k < 9; k++){
            if(k == del1 || k == del2){
    			continue;
            }
            System.out.println(dwarfs[k]);
            
        }
		
    }
}