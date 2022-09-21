import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cup = 1;
        for(int i=0; i<n; i++){
            int x = sc.nextInt();
            int y = sc.nextInt();
            if(cup == x) cup = y;
            else if(cup == y) cup = x;
        }
        System.out.println(cup);
    }
}