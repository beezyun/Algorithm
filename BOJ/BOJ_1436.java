// https://www.acmicpc.net/problem/1436
// Silver 5 영화감독 숌

import java.util.Scanner;

public class BOJ_1436 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int num = sc.nextInt();
		int count = 0;
		
		int i = 666;
		while (true) {
			String str = Integer.toString(i);
			
			if (str.contains("666")) {
				count++;
				
				if (count == num) {
					System.out.println(i);
					break;
				}
			}
			
			i++;
		}

	}

}
