import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        int n = nums.length / 2;
        
        Set<Integer> pokemon = new HashSet<>();
        
        for(int num : nums){
            pokemon.add(num);
        }
        
        return Math.min(n, pokemon.size());
        
    }
}