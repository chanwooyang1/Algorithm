import java.util.*;
class Solution {
    public int solution(int N, int number) {
        int answer = 0;
        Set<Integer>[] arr =  new HashSet[9];
        
        for(int i = 1; i<= 8; i++){
            arr[i] = new HashSet<>();
            arr[i].add(Integer.valueOf(String.valueOf(N).repeat(i)));
        }
       
        for(int i = 1; i <= 8; i++){
            for(int j = 1; j < i; j++){
                for(int a : arr[j]){
                    for(int b : arr[i - j]){
                    arr[i].add(a + b);
                    arr[i].add(a - b);
                    arr[i].add(a * b);
                    if(b != 0){
                        arr[i].add(a / b);
                    }
                    }
                }
            }
            if(arr[i].contains(number)){
                return i;
            }
        }
        
       
        return -1;
    }
}