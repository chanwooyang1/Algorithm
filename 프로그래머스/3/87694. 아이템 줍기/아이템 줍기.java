import java.util.*;
class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int size = 102; //범위가 1부터 50까지니까 배열로 하면 51사이즈로 해야 1부터 50 하지만 경계를 명확하게 하기위해 2배인 102
        boolean[][] visited = new boolean[size][size];
        boolean[][] maps = new boolean[size][size];
        
        int[] dx = {0,0,-1,1};
        int[] dy = {-1,1,0,0};
        
        for(int[] rect : rectangle){
            int x1 = rect[0] * 2; //좌표도 다 2배
            int y1 = rect[1] * 2;
            int x2 = rect[2] * 2;
            int y2 = rect[3] * 2;
            
            for(int i = x1; i <= x2; i++){ //왼쪽아래 좌표부터 오른쪽 위좌표까지 전체를 true로 칠하기
                for(int j = y1; j <= y2; j++){
                    maps[i][j] = true;
                }
            }
        }
            
        for(int[] rect : rectangle){ // 전체 칠한 칸에서 한칸씩 안으로 들어와서 다시 false로 칠해서 경계 한칸만 남기기
            int x1 = rect[0] * 2;
            int y1 = rect[1] * 2;
            int x2 = rect[2] * 2;
            int y2 = rect[3] * 2;
            
            for(int i = x1 + 1; i < x2; i++){
                for(int j = y1 + 1; j < y2; j++){
                    maps[i][j] = false;
                }
            }
        }
            
            Queue<int[]> q = new LinkedList<>(); // 큐 만들고 맨 처음 좌표 집어넣고 방문처리
            q.offer(new int[]{characterX * 2, characterY * 2, 0});
            visited[characterX * 2][characterY * 2] = true;
            
            
            while(!q.isEmpty()){ 
                int[] current = q.poll();
                int x = current[0];
                int y = current[1];
                int distance = current[2];
                
                if(x == 2 * itemX && y == 2 * itemY){ //큐 돌다가 목표 지점에 도착하면 결과 리턴
                    return distance / 2;
                }
                
                for(int i = 0; i < 4; i++){ //4방향을 돌면서
                    int nx = x + dx[i];
                    int ny = y + dy[i];
                    
                    if(nx >= 0 && ny >= 0 && nx < size && ny < size && maps[nx][ny] && !visited[nx][ny]){// nx랑 ny가 범위안에 있고 테두리이며 방문하지 않았다면 방문처리후 큐에 삽입
                       
                        visited[nx][ny] = true; 
                        q.offer(new int[]{nx, ny, distance + 1});
                    }
                    
                }
                
                
            }return -1; // 문제 조건상 항상 목적지는 테두리 위에 존재하지만 만약 구하지 못한다면 -1을 리턴하도록 체크
        
            
            
        }
    }

