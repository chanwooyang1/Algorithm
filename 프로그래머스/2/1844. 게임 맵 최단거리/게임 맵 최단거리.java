import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        boolean[][] visited = new boolean[n][m];
        int answer = 0;
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        Queue<int[]> queue = new LinkedList<>(); 
        queue.offer(new int[]{0,0,1});
        
        while(!queue.isEmpty()){
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int distance  = current[2];
            
            
            if(x == n-1&& y == m-1){
                return distance;
            }
            
            for(int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if(nx >= 0&& nx < n && ny >=0 && ny < m && !visited[nx][ny] && maps[nx][ny] == 1){
                    queue.offer(new int[]{nx,ny,distance + 1});
                    visited[nx][ny] = true;
                }
            }
            
            
            
        }
        return -1;
    }
}