import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int[] alphabet = new int[26];
        while(sc.hasNextLine()){
            String s = sc.nextLine();
            for (int i = 0; i < s.length(); i++){
                if (s.charAt(i) >= 'a' && s.charAt(i) <= 'z'){
                    alphabet[s.charAt(i)-'a']++;
                }
            }
        }
        int max = 0;
        for (int i = 0; i< 26; i++){
            if (max < alphabet[i]){
                max = alphabet[i];
            }
        }
        for (int i=0; i<26; i++){
            if (max == alphabet[i]){
                System.out.print((char)(i+'a'));
            }
        }

        
    }
}
