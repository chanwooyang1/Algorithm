class Solution {
    public int solution(int[][] sizes) {
        int maxP = 0;
        int maxV = 0;
        for(int[] size : sizes){
            int p = size[0];
            int v = size[1];
            if(p < v){
                int temp = p;
                p = v;
                v = temp;
            }
            maxP = Math.max(maxP, p);
            maxV = Math.max(maxV, v);
        }
        return maxP * maxV;
    }
}