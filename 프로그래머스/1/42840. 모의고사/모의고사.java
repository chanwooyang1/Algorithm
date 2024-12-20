import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] one = {1,2,3,4,5};
        int[] two = {2,1,2,3,2,4,2,5};
        int[] three= {3,3,1,1,2,2,4,4,5,5};
        int[] points = new int[3];
        for(int i = 0; i < 3; i++){
            int maxPoint = 0;
            for(int j = 0; j < answers.length; j++){
                
                if(i == 0){
                    if(answers[j] == one[j % 5]){
                        maxPoint++;
                    }
                }else if(i == 1){
                    if(answers[j] == two[j % 8]){
                        maxPoint++;
                    }
                }else if(i == 2){
                    if(answers[j] == three[j % 10]){
                        maxPoint++;
                    }
                }
            }points[i] = maxPoint;
        }
        
        
        int maxGrade = 0;
        for(int i = 0; i < 3; i++){
            maxGrade = Math.max(maxGrade, points[i]);
        }
        List<Integer> answer = new ArrayList<>();
        for(int i = 0; i < 3; i++){
            if(points[i] == maxGrade){
                answer.add(i+1);
            }
        }
        int[] result = answer.stream().mapToInt(Integer::intValue).toArray();
        return result;
    }
}