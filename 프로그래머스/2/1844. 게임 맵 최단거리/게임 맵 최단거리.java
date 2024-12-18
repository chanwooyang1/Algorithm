import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] visited = new boolean[n][m]; //방문 처리를 위해 boolean 
        Queue<int[]> queue = new LinkedList<>(); // 모든 경우의 수를 돌기위해 queue 사용
        
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        
        
        queue.offer(new int[]{0,0,1}); //초기 값 세팅
        visited[0][0] = true;
        
        while(!queue.isEmpty()){ // queue가 채워져있는동안 돌기, 만약 queue가 비워졌는데 목표하는 곳에 도달하지 못하면 
            int[] current = queue.poll();// return값이 없으므로 외부에서 처리
            int x = current[0];
            int y = current[1];
            int distance  = current[2]; // queue에서 하나 꺼내서 값 정리
            
            
            if(x == n-1&& y == m-1){ //목표에 도달하면 최단거리 값 출력
                return distance;
            }
            
            for(int i = 0; i < 4; i++){ //4방향을 돌면서
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx >= 0&& nx < n && ny >=0 && ny < m && !visited[nx][ny] && maps[nx][ny] == 1){// 조건에 맞다면 
                    queue.offer(new int[]{nx,ny,distance + 1}); //큐에 집어넣고 방문처리
                    visited[nx][ny] = true;
                }
            }
            
        }
        return -1;
    }
}