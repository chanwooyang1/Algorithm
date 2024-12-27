import java.util.*;
class Solution {
    public int solution(String[] friends, String[] gifts) {
        int answer = 0;
        int n = friends.length;
        
        
        Map<String, Integer> pointMap = new HashMap<>();
        Map<String, Map<String, Integer>> gtMap = new HashMap<>();
        
        for(String name: friends){
            pointMap.put(name, 0);
            gtMap.put(name, new HashMap<>());
            for(String name2 : friends){
                gtMap.get(name).put(name2, 0);
            }   
        }
        
        for(String gift : gifts){
            String[] splitName = gift.split(" ");
            String from = splitName[0];
            String to = splitName[1];
            
            pointMap.put(from, pointMap.get(from) + 1);
            pointMap.put(to, pointMap.get(to) - 1);
            
            gtMap.get(from).put(to, gtMap.get(from).get(to) + 1);
            
            }
        
        int maxPoint = 0;
        for(String name: friends){
            int currentPoint = 0;
            Map<String, Integer> points = gtMap.get(name);
            for(Map.Entry<String, Integer> entry : points.entrySet()){
                String key = entry.getKey();
                Integer value = entry.getValue();
                System.out.println("name: " + name+ " key: " + key+ " value: " + value);
                if(!key.equals(name)){
                    if(value > gtMap.get(key).get(name)){
                        currentPoint++;
                        System.out.println("조건1");
                    }else if(value == gtMap.get(key).get(name) 
                             && pointMap.get(name) > pointMap.get(key)){
                        currentPoint++;
                        System.out.println("조건2");
                    }
                }
                
                
            }System.out.println("name: " + name + " currentPoint: " + currentPoint);
            
            maxPoint = Math.max(maxPoint, currentPoint);
        }
        
        
        
        
        return maxPoint;
    }
}