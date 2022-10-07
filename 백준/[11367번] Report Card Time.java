import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		String in = sc.nextLine();
		int num = Integer.parseInt(in);
		for(int i=0; i<num; i++){
			String sentence = sc.nextLine();
			String[] arr = sentence.split(" ");
			String name = arr[0];
			int score = Integer.parseInt(arr[1]);
			String grade = "";
			
			if(0 <= score && score <= 59) grade = "F";
			else if(60 <= score && score <= 66) grade = "D";
			else if(67 <= score && score <= 69) grade = "D+";
			else if(70 <= score && score <= 76) grade = "C";
			else if(77 <= score && score <= 79) grade = "C+";
			else if(80 <= score && score <= 86) grade = "B";
			else if(87 <= score && score <= 89) grade = "B+";
			else if(90<= score && score <= 96) grade = "A";
			else if(97 <= score && score <= 100) grade = "A+";
			
			System.out.printf("%s %s\n", name , grade);
		}
	}
}