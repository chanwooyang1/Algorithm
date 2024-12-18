import java.util.*;
class Solution {
    int answer = 0;
        
    public int solution(int[] numbers, int target) {
        
        dfs(numbers, target, 0, 0);
        
        
        return answer;
    }
    
    private void dfs(int[] numbers, int target, int index, int sum){
        if(index == numbers.length){ // 배열을 다 돌았을때
            if(sum == target){ // 값이 타겟팅된다면 정답++
                answer++;
            }
            return; // 값이 맞던 안맞던 배열을 다 돌면 종료해야 하므로 else 없이 리턴
                
            
        }
        dfs(numbers, target, index + 1, sum + numbers[index]); //더하거나
        dfs(numbers, target, index + 1, sum - numbers[index]);// 빼거나 
        
    }
}