import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer[]> list = new ArrayList<>();
        for(int i = 0; i < N; i++){
            String[] numbers = br.readLine().split(" ");
            list.add(new Integer[]{Integer.parseInt(numbers[0]), Integer.parseInt(numbers[1])});
        }
        list.sort((a,b) -> {
            int cmp  = Integer.compare(a[1], b[1]);
            if(cmp == 0){
                return Integer.compare(a[0], b[0]);
            }
            return cmp;
        });
        for(int j = 0; j < N; j++){
            System.out.println(list.get(j)[0] + " " + list.get(j)[1]);
        }
    }
}