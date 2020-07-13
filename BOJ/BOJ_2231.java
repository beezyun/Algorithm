import java.util.Scanner;

// Bronze 2 분해합
public class BOJ_2231 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		int m = sc.nextInt();
		int isNull = 1;
		int min = 0;
		
		for (int i = 1; i <= 1000000; i++) {
			if (calc(i) == m) {
				if (isNull == 1) {
					min = i;
					isNull = 0;
				} else if (i < min) {
					min = i;
				}
			}
		}
		
		System.out.println(min);

	}
	
	public static int calc(int n) {
		
		int digit = (int) Math.log10(n) + 1; // n의 자릿수
		int result = n;		

		for (int i = 0; i < digit; i++) {
			result = result + (n % 10);
			n = n / 10;
		}
		
		return result;
		
	}

}
