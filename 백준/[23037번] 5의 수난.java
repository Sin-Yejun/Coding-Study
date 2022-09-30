import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		String num = sc.nextLine();
		int answer = 0;
		for(int i=0; i<num.length(); i++){
			answer += Math.pow((int)(num.charAt(i))-48,5);
		}
		System.out.println(answer);
	}

}