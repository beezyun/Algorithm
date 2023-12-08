// https://school.programmers.co.kr/learn/courses/30/lessons/42862
// Lv.1 체육복

import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = n - lost.length;

        Arrays.sort(lost);
        Arrays.sort(reserve);
        ArrayList<Integer> lostArr = new ArrayList<>();
        ArrayList<Integer> reserveArr = new ArrayList<>();

        for(int i = 0; i < lost.length; i++) {
            lostArr.add(lost[i]);
        }

        for(int i = 0; i < reserve.length; i++) {
            reserveArr.add(reserve[i]);
        }

        // System.out.println(lostArr);
        // System.out.println(reserveArr);

        // 여벌 체육복을 가져온 학생이 체육복을 도난당한 경우
        for (int lostStu : lost) {
            if (reserveArr.contains(lostStu)) {
                answer++;
                reserveArr.remove(Integer.valueOf(lostStu));
                lostArr.remove(Integer.valueOf(lostStu));
            }
        }

        // System.out.println(lostArr);

        for (int lostArrStu : lostArr) {
            if (lostArrStu != 1 && reserveArr.contains(lostArrStu - 1)) {
                answer++;
                reserveArr.remove(Integer.valueOf(lostArrStu - 1));
            } else if (lostArrStu != n && reserveArr.contains(lostArrStu + 1)) {
                answer++;
                reserveArr.remove(Integer.valueOf(lostArrStu + 1));
            }
        }

        return answer;
    }
}