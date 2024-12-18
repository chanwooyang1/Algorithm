import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        if(!Arrays.asList(words).contains(target)){
            return 0;
        }
        
        boolean[] visited = new boolean[words.length];
        Queue<String> queue = new LinkedList<>();
        
        queue.offer(begin);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            for(int i = 0; i < size; i++){
                String current = queue.poll();
                
                if(current.equals(target)){
                    return answer;
                }
                
                for(int j = 0; j < words.length; j++){
                    String other = words[j];
                    if(check(current, other) && !visited[j]){
                        queue.offer(other);
                        visited[j] = true;
                        System.out.println(other);
                    }
                }
            }answer++;
            
        }
        
        return answer;
    }
    private boolean check(String word, String other){
        int count = 0;
        for(int i = 0; i < word.length(); i++ ){
            if(count >= 2){
                return false;
            }
            if(word.charAt(i) != other.charAt(i)){
                count++;
            }
        }
        if(count == 1){
            return true;
        }else{
            return false;
        }
    }
}