import java.util.*;
class Solution {
    int answer = 0; 
    boolean[] visited;
    public int solution(int n, int[][] computers) {
       visited = new boolean[n];
        for(int i = 0; i < n; i++){
            if(!visited[i]){
                 dfs(computers, i);
                answer++;
            }
        }
       
        
        return answer;
    }
    private void dfs(int[][] computers, int index){
        visited[index] = true;
        int[] computer = computers[index];
        for(int i = 0; i < computer.length; i++){
            if(computer[i] == 1 && !visited[i]){
                dfs(computers, i);
            }
        }
    }
}