// https://school.programmers.co.kr/learn/courses/30/lessons/12906
// Lv.1 같은 숫자는 싫어

import java.util.*;

class Solution {
    public int[] solution(int []arr) {
        int[] answer;
        ArrayList<Integer> answerTmp = new ArrayList<>();
        
        int tmp = arr[0]; // tmp를 arr[0]으로 초기화 한 후
        for(int i = 1; i < arr.length; i++) { // index: 1부터 반복문을 돌면서 arr 배열의 값을 비교
            if (tmp == arr[i]) { // tmp와 현재 index의 값이 같으면 (연속적으로 나타나는 숫자이면)
                arr[i] = -1; // arr 배열의 해당 index의 값을 -1로 대체
            } else { // tmp와 현재 index의 값이 같지 않으면
                tmp = arr[i]; // tmp에 현재 index의 값(다음 연속 여부를 확인할 값)을 할당
            }
        }
        
        // arr 배열에서 -1이 아닌 값을 answerTmp에 할당
        for(int i = 0; i < arr.length; i++) {
            if (!(arr[i] == -1))
                answerTmp.add(arr[i]);
        }
        
        // answerTmp의 값들을 answer에 복사
        answer = new int[answerTmp.size()];
        for(int i = 0; i < answer.length; i++) {
            answer[i] = answerTmp.get(i);
        }
        
        return answer;
    }
}