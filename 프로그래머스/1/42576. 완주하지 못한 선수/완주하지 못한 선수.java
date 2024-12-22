import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        Map<String, Integer> pMap = new HashMap<>();
        
        for(String name : participant){
            pMap.put(name, pMap.getOrDefault(name, 0) + 1);
        }
        
        for(String comp : completion){
            pMap.put(comp, pMap.get(comp) - 1);
        }
        
        for(Map.Entry<String, Integer> entry: pMap.entrySet()){
            if(entry.getValue() == 0){
                continue;
            }
            return entry.getKey();
        }
        return null;
        
    
}
}