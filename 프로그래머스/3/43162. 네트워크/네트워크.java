import java.util.*;
class Solution {
    int answer = 0; 
    boolean[] visited;
    public int solution(int n, int[][] computers) {
       visited = new boolean[n]; //각각의 컴퓨터를 거쳤는지 확인하기 위해체크
        for(int i = 0; i < n; i++){ //컴퓨터를 0번부터 돌면서
            if(!visited[i]){  // 만약 거치지 않았다면
                 dfs(computers, i); //로직 실행
                answer++; // 끝까지 탐색후 돌아와서 네트워크 개수 추가
            }
        }
       
        return answer;
    }
    private void dfs(int[][] computers, int index){
        visited[index] = true; // 방문처리하고
        for(int i = 0; i < computers.length; i++){ //해당 컴퓨터랑 연결된 컴퓨터 조사
            if(computers[index][i] == 1 && !visited[i]){ //연결되어있으면서 방문하지 않았다면
                dfs(computers, i); // 한번 더 dfs 들어가기
            }
        }
    }
} 