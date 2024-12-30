class Solution {
    public int solution(int n) {
        int MOD = 1000000007;
        long[] dp = new long[n + 1];
        dp[0] = 1;
        dp[2] = 3;
        for(int i = 4; i <= n; i++){
            if(i % 2 != 0){
                dp[i] = 0;
                continue;
            }else{
              dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % MOD;  
               if(dp[i] < 0){
                   dp[i] += MOD;
               } 
            }
            
        }
        return (int)dp[n];
    }
}