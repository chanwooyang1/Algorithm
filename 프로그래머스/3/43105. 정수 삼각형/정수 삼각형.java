import java.util.*;
class Solution {
    public int solution(int[][] triangle) {
        int n = triangle.length;
        int answer = triangle[0][0];
        int[][] dp = new int[n][n];
        dp[0][0] = answer;
        
        
        for(int i = 0; i < triangle.length - 1; i++){
            for(int j = 0; j <= i; j++){
                dp[i+1][j] = Math.max(dp[i+1][j], triangle[i+1][j] + dp[i][j]);
                dp[i+1][j+1] = Math.max(dp[i+1][j+1], triangle[i+1][j+1] + dp[i][j]);
            }
        }
        for(int k = 0; k < n; k++){
            answer = Math.max(answer, dp[n-1][k]);
        }
        
        
        return answer;
    }
}