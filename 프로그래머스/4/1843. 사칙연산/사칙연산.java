class Solution {
    public int solution(String arr[]) {
        int n = (arr.length + 1) /2;
        
        int[][] maxDp = new int[n][n];
        int[][] minDp = new int[n][n];
        
        for(int i = 0; i < n; i++){
            int num = Integer.parseInt(arr[2*i]);
            maxDp[i][i] = num;
            minDp[i][i] = num;
        }
        
        for(int size = 1; size < n; size++){ //구간 크기
            for(int i = 0; i < n - size; i++){ // 시작점, 범위는 구간크기를 수용할수 있는 최대 시작점의 범위
                int j = size + i;//끝점 
                maxDp[i][j] = Integer.MIN_VALUE;
                minDp[i][j] = Integer.MAX_VALUE;
                
                for(int k = i; k < j; k++){// i-j 를 i-k, k+1 - j 로 나눠주기
                    char operator = arr[2 * k + 1].charAt(0);
                    
                     if (operator == '+') {
                        maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] + maxDp[k+1][j]);
                        minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] + minDp[k+1][j]);
                    } else if (operator == '-') {
                        maxDp[i][j] = Math.max(maxDp[i][j], maxDp[i][k] - minDp[k+1][j]);
                        minDp[i][j] = Math.min(minDp[i][j], minDp[i][k] - maxDp[k+1][j]);
                    }
                    
                }
                
                
            }
        }
        
        return maxDp[0][n-1];
    }
}