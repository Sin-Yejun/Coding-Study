import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		st = new StringTokenizer(br.readLine());
		long a = Long.parseLong(st.nextToken());
		long b = Long.parseLong(st.nextToken());
		long A = Math.min(a,b);
		long B = Math.max(a,b);
		if(A==B){
			bw.write('0');
		}
		else{
			bw.write((long)(B-A-1)+"\n");
			for(long i = A+1; i<B; i++){
				bw.write(i+" ");
			}
		}
		bw.flush();
		bw.close();
	}

}