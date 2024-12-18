import java.util.*;
class Solution {
    public int solution(String begin, String target, String[] words) {
        int answer = 0;
        if(!Arrays.asList(words).contains(target)){ // 만약 target이 들어있지 않다면 0 출력
            return 0;
        }
        
        boolean[] visited = new boolean[words.length];
        Queue<String> queue = new LinkedList<>();
        queue.offer(begin);
        
        while(!queue.isEmpty()){
            int size = queue.size(); // queue가 int queue이면 항목을 추가해서 횟수를 계산할수 있지만 String queue이기 때문에 따로 루프를 주어서 횟수를 계산
            for(int i = 0; i < size; i++){
                String current = queue.poll();
                
                if(current.equals(target)){ //문제 풀때 까먹었던 최종 조건 설정
                    return answer;
                }
                
                for(int j = 0; j < words.length; j++){
                    String other = words[j];
                    if(check(current, other) && !visited[j]){ //조건 검사하고 방문하지 않았다면 큐에 삽입
                        queue.offer(other);
                        visited[j] = true;
                    }
                }
            }answer++;
            
        }
        
        return answer;
    }
    private boolean check(String word, String other){ // 단어 두개를 비교해서 다른 철자가 1개인지 체크
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