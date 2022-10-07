import java.util.*;
import java.io.*;
public class Main {
	
	public static void main(String[] args) throws IOException {
		Scanner sc = new Scanner(System.in);
		String in = sc.nextLine();
		int num = Integer.parseInt(in);
		for(int i=0; i<num; i++){
			String sentence = sc.nextLine().trim().toLowerCase().replaceAll(" ", "");
			int con = 0, vow = 0;
			for(int j=0; j<sentence.length(); j++){
				switch(sentence.charAt(j)){
					case 'a':
					case 'e':
					case 'i':
					case 'o':
					case 'u':
						vow ++;
						break;
					default:
						con++;
				}
			}
			System.out.printf("%d %d\n", con , vow);
		}
	}
}