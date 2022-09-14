import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        while(true){
            String sentence = sc.nextLine();
    
            int cnt = 0;
            if(sentence.equals("#")){
                break;
            }
            for(int i=0; i<sentence.length(); i++){
                char c = sentence.charAt(i);
                if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U'){
                    cnt += 1;
                }
            }
            System.out.println(cnt);
        }

        
    }
}
