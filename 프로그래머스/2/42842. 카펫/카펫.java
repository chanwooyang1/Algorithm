class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {};
        int total = brown + yellow;
        for(int height = 1; height < total /2 + 1; height++){
            if(total % height == 0){
                int width = total / height;
                if((2 * width ) + (2 * height) - 4 == brown){
                    return new int[]{width, height};
                }
            }
        }
        return answer;
       
    }
}