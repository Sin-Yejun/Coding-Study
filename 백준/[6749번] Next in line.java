import java.util.Scanner;
public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);
        int age1 = sc.nextInt();
        int age2 = sc.nextInt();
        int diff = age2 - age1;
        System.out.println(age2 + diff);
    }
     
}