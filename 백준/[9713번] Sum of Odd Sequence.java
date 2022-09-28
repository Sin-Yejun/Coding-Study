import java.util.*;
public class Main {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int N = sc.nextInt();
		
		for(int i=0; i<N; i++){
			int num = sc.nextInt();
			int answer = ((num-1)/2) +1;
			System.out.println(answer*answer);
		}
	}

}