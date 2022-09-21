import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int sec = 0;
        int sum = 0;
        int cnt = 1;
        while(true){
            if(n==sum){
                System.out.println(sec);
                break;
            }
            sec ++;
            if(sum+cnt > n) cnt = 1;
            sum += cnt;
            cnt++;
        }
    }
}