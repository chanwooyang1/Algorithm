import java.util.*;
class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long q1Sum = Arrays.stream(queue1).sum();
        long q2Sum = Arrays.stream(queue2).sum();
        long target = (q1Sum + q2Sum) /2;
        int n =  queue1.length;
        int[] circle = new int[2 * n];
        
        for(int i = 0; i < n; i++){
            circle[i] = queue1[i];
        }
        for(int j = 0; j < n; j++){
            circle[j + n] = queue2[j];
        }
        int l1 = 0;
        int r1 = n - 1;
        
        int l2 = n;
        int r2 = 2 * n - 1;
        
        if((q1Sum + q2Sum) % 2 != 0){
            return -1;
        }
        
        while(answer < 4 * n){
            if(q1Sum < target){
                r1 = (r1 + 1) % circle.length;
                l2 = (l2 + 1) % circle.length;
                
                q1Sum += circle[r1];
                q2Sum -= circle[r1];
                
                answer++;
                
            }
            
            if(q2Sum < target){
                r2 = (r2 + 1) % circle.length;
                l1 = (l1 + 1) % circle.length;
                
                q2Sum += circle[r2];
                q1Sum -= circle[r2];
                
                answer++;
            }
            
            if(q1Sum == target && q2Sum == target){
                return answer;
            }
        }
        
        
        return -1;
    }
    
   
}