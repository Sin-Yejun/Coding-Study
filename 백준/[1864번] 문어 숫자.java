import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter wr = new BufferedWriter(new OutputStreamWriter(System.out));
        int cnt = 0;
        int sum = 0;
        while(true){
            String input = br.readLine();
            if(input.equals("#")) break;
            for(int i=0; i<input.length(); i++){
                int temp = 0;
                switch(input.charAt(i)){
                    case '-':
                        temp = 0; break;
                    case '\\':
                        temp = 1; break;
                    case '(':
                        temp = 2; break;
                    case '@':
                        temp = 3; break;
                    case '?':
                        temp = 4; break;
                    case '>':
                        temp = 5; break;
                    case '&':
                        temp = 6; break;
                    case '%':
                        temp = 7; break;
                    case '/':
                        temp = -1; break;
                }
                sum += temp*Math.pow(8, input.length()-1-cnt);
                cnt ++;
                    
            }
            wr.write(sum+"\n");
            cnt = 0;
            sum = 0;
        }
        wr.flush();
        wr.close();
    }

}
