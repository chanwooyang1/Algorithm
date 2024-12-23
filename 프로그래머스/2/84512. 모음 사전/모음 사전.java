class Solution {
    public int solution(String word) {
        
        char[] vowels = {'A', 'E', 'I', 'O', 'U'};
        int[] weights = {781, 156, 31, 6, 1}; // 각 자릿수의 가중치
        int answer = 0;
        
        for(int i = 0; i < word.length(); i++){
            char ch = word.charAt(i);
            int position = new String(vowels).indexOf(ch);
            answer += position * weights[i] + 1;
        }
        return answer;
    }
}