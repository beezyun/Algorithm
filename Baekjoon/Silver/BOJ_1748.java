// https://www.acmicpc.net/problem/1748
// Silver 4 수 이어 쓰기 1

import java.util.Scanner;

public class BOJ_1748 {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int digit = Integer.toString(num).length();
		
		/*
		for (int i = 1; i <= num; i++) {
			digit += Integer.toString(i).length();	// 메모리 초과
			digit += (int)(Math.log10(i) + 1);	// 시간 초과
		}
		*/
		
//		1 ~ 9		: 9
//		10 ~ 99		: 90
//		100 ~ 999	: 900
//		...
		
		int result = 0;
		for (int i = 1; i < digit; i++) {
			result = result + (int)(i * 9 * Math.pow(10, i - 1));
		}
		
		// 마지막 자릿 수
		result = result + (int)(digit * (num - Math.pow(10, digit - 1) + 1));
		
		System.out.println(result);
		
	}

}
