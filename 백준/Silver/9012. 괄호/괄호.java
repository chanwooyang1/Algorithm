import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(br.readLine());
        for(int i = 0; i < N; i++){
            String line = br.readLine();
            int length = line.length();
            Deque<Character> st = new ArrayDeque<>();
            for(int j = 0; j < length; j++){
                char ch = line.charAt(j);
                if(ch == '('){
                    st.push(ch);
                }else{
                    if(!st.isEmpty()){
                        st.pop();
                    }else{
                    	st.push(ch);
                        break;
                    }
                }
            }
            if(st.isEmpty()){
                System.out.println("YES");
            }else {
                System.out.println("NO");
            }
        }
    }
}