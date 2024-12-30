class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        for(int num : num_list){
            int count = 0;
            while(num != 1){
                System.out.println("num: " + num);
                if(num % 2 == 0){
                    num = num / 2;
                    count++;
                }else{
                    num -= 1;
                    num = num / 2;
                    count++;
                }
            }answer += count;
            System.out.println(count);
        }
        return answer;
    }
}