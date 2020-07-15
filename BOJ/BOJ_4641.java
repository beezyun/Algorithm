import java.util.Scanner;

// https://www.acmicpc.net/problem/4641
// Bronze 1 Doubles
public class BOJ_4641 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			int count = 0;
			String str = sc.nextLine();
			
			if (str.equals("-1"))
				break;
			
			String[] strArr = str.split(" ");
			int[] intArr = new int[strArr.length - 1]; // 마지막 index 값인 0 제외
			
			// String 배열을 int 배열로 변환
			for (int i = 0; i < intArr.length; i++) {
				intArr[i] = Integer.valueOf(strArr[i]);
			}
			
			for (int i = 0; i < intArr.length; i++) {
				for (int j = 0; j < intArr.length; j++) {
					if ((intArr[i] * 2) == intArr[j]) {
						count++;
						break;
					}
				}
			}
			
			System.out.println(count);
		}

	}

}
