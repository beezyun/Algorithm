// https://www.acmicpc.net/problem/1085
// Bronze 3 직사각형에서 탈출

import java.util.Scanner;

public class BOJ_1085 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();
        int w = sc.nextInt();
        int h = sc.nextInt();
        int minX, minY;

        // X축 최소값 구하기
        if(x - 0> w - x)
            minX = w - x;
        else
            minX = x - 0;

        // Y축 최소값 구하기
        if(y - 0 > h - y)
            minY = h - y;
        else
            minY = y - 0;

        // X축 최소값과 Y축 최소값 비교 후 최종 최소값 구하기
        if(minX > minY)
            System.out.print(minY);
        else
            System.out.print(minX);
    }
}