class Solution {
    public int solution(String name) {
        int len = name.length();
        int answer = 0;
        
        // 알파벳 변경 횟수 계산
        for (int i = 0; i < len; i++) {
            char c = name.charAt(i);
            int move = Math.min(c - 'A', 'Z' - c + 1);
            answer += move;
        }

        // 커서 이동 최소화 계산
        int minMove = len - 1; // 오른쪽으로만 이동할 경우

        for (int i = 0; i < len; i++) {
            int next = i + 1;
            while (next < len && name.charAt(next) == 'A') {
                next++;
            }
            int move = i + len - next + Math.min(i, len - next);
            minMove = Math.min(minMove, move);
        }

        answer += minMove;
        return answer;
    }
}