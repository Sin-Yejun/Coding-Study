import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		for(int i=0; i<num; i++){
			String binary = sc.next();
			System.out.println(Integer.parseInt(binary,2));
		}
	}
}