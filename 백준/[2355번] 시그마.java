import java.util.*;
import java.io.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine()+" ");
        long n1 = Long.parseLong(st.nextToken());
        long n2 = Long.parseLong(st.nextToken());
        long A = Math.min(n1,n2);
        long B = Math.max(n1,n2);
        long sum = (((B + 1) * B) / 2) - (((A - 1) * A) / 2);
        bw.write(sum+"\n");
        bw.flush();
        bw.close();
    }

}
