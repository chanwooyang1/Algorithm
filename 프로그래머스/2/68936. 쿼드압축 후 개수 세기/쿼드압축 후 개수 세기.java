class Solution {
    int[] answer = new int[2];
    public int[] solution(int[][] arr) {
        int length = arr.length;
        quadZip(arr, 0, 0, length);
        
        
        return answer;
    }
    private void quadZip(int[][] arr, int x, int y, int length){
        if(check(arr, x, y, length, arr[x][y])){
            if(arr[x][y] == 1){
                answer[1]++;
            }else{
                answer[0]++;
            }
            return;
        }
        quadZip(arr, x, y, length/2);
        quadZip(arr, x + length/2 , y, length/2);
        quadZip(arr, x, y + length/2, length/2);
        quadZip(arr, x + length/2 , y + length/2 , length/2);
        
    }
    
    
    private boolean check(int[][] arr, int x, int y , int length, int arrVal){
        for(int i = x; i < x + length; i++){
            for(int j = y; j < y + length; j++){
                if(arr[i][j] != arrVal){
                    return false;
                }
            }
        }return true;
    }
}