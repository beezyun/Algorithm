// https://www.acmicpc.net/problem/6679
// Bronze 2 싱기한 네자리 숫자

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_6679 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		List<Integer> arr = new ArrayList<Integer>();

		String str12, str16;
		int sum10, sum12, sum16;
		
		for (int i = 1000; i <= 9999; i++) {
			
			str12 = Integer.toString(i, 12);
			str16 = Integer.toString(i, 16);
			
			sum10 = digitSum10(i);
			sum12 = digitSum12(str12);
			sum16 = digitSum16(str16);
			
			if (sum10 == sum12 && sum12 == sum16)
				arr.add(i);
		}
		
		Collections.sort(arr);
		for (int i = 0; i < arr.size(); i++) {
			System.out.println(arr.get(i));
		}

	}
	
	// 10진수 자릿수 더하기
	public static int digitSum10(int num) {
		
		int digit = (int) Math.log10(num) + 1;
		int sum = 0;
		
		for (int i = 0; i < digit; i++) {
			sum = sum + (num % 10);
			num = num / 10;
		}
		
		return sum;
	}
	
	// 12진수 자릿수 더하기
	public static int digitSum12(String str) {
		
		char ch;
		int temp;
		int sum = 0;
		
		for (int i = 0; i < str.length(); i++) {
			ch = str.charAt(i);
			
			switch(ch) {
				case 'a':
					temp = 10;
					break;
				case 'b':
					temp = 11;
					break;
				default:
					temp = (int) ch - '0';
					break;
			}
			
			sum = sum + temp;
		}
		
		return sum;
	}
	
	// 16진수 자릿수 구하기
	public static int digitSum16(String str) {
		
		char ch;
		int temp;
		int sum = 0;
		
		for (int i = 0; i < str.length(); i++) {
			ch = str.charAt(i);
			
			switch(ch) {
				case 'a':
					temp = 10;
					break;
				case 'b':
					temp = 11;
					break;
				case 'c':
					temp = 12;
					break;
				case 'd':
					temp = 13;
					break;
				case 'e':
					temp = 14;
					break;
				case 'f':
					temp = 15;
					break;
				default:
					temp = (int) ch - '0';
					break;
			}
			
			sum = sum + temp;
		}
		
		return sum;
	}

}
