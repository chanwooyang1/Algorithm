import java.util.*;
class Solution {
    Map<String, PriorityQueue<String>> map = new HashMap<>();
    List<String> answer = new ArrayList<>();
    public String[] solution(String[][] tickets) {
        
        for(String[] ticket : tickets){ // 출발지를 key로 도착지를 value로 저장하기
            String from = ticket[0];    //priorityQueue를 사용하면 오름차순 정리
            String to = ticket[1];
           map.putIfAbsent(from, new PriorityQueue<>());
            map.get(from).offer(to);
        }
        
        dfs("ICN");
        return answer.toArray(new String[0]); //리스트를 배열로 만들기 작은 사이즈의 배열을 넣으면 알아서 사이즈를 맞춤
    }
    
    private void dfs(String current){ // 현재 도시를 key로 value를 찾아서 dfs반복 
        PriorityQueue<String> pq = map.get(current);
        while(map.containsKey(current) && !pq.isEmpty()){
            String next = pq.poll();
            System.out.println(next);
            dfs(next);
            
        }
        answer.add(0, current);
    }

}