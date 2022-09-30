import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		int num = sc.nextInt();
		System.out.print(Math.round(num*0.78)+" ");
		System.out.println(num - Math.round(num*0.2*0.22));
	}

}