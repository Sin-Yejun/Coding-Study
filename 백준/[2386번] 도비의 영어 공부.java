import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        while (true){
            String input = br.readLine();
            if(input.equals("#")) break;
            StringTokenizer st = new StringTokenizer(input, " ");
            char letter = st.nextToken().charAt(0);
            String str = "";
            while (st.hasMoreTokens()){
                str += st.nextToken();
            }
            int cnt = 0;
            for(char l: str.toLowerCase().toCharArray()){
                if(letter == l) cnt ++;
            }
            System.out.println(letter+" "+cnt);
        }
    }

}
