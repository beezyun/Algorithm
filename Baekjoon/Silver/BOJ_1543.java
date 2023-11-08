// https://www.acmicpc.net/problem/1543
// Silver 5 문서 검색

import java.util.Scanner;

public class BOJ_1543 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String word = sc.nextLine();
        String search = sc.nextLine();
        int count = 0;

        while(word.indexOf(search) >= 0) {
            count++;
            word = word.substring(word.indexOf(search) + search.length());
        }
        System.out.println(count);
    }
}