// https://www.acmicpc.net/problem/1620
// Silver 4 나는야 포켓몬 마스터 이다솜

import java.io.*;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;
import java.util.StringTokenizer;

public class BOJ_1620 {
    public static void main(String[] args) throws IOException {
        /* 첫 번째 풀이 시간 초과 오류
        Scanner sc = new Scanner(System.in);

        int pokemonNum = sc.nextInt();
        int problemNum = sc.nextInt();
        ArrayList pokemonArr = new ArrayList<String>();
        ArrayList resultArr = new ArrayList<String>();

        for (int i = 0; i < pokemonNum; i++) {
            String pokemonName = sc.next();
            pokemonArr.add(pokemonName);
        }

        // 문제에 대한 답을 배열로 생성
        for (int i = 0; i < problemNum; i++) {
            String str = sc.next();
            if(isString(str)) {
                resultArr.add(pokemonArr.indexOf(str) + 1);
            } else {
                resultArr.add((pokemonArr.get(Integer.parseInt(str) - 1)));
            }
        }

        // 결과 출력
        for (Object str : resultArr) {
            System.out.println(str);
        }
        */

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int pokemonNum = Integer.parseInt(st.nextToken());
        int problemNum = Integer.parseInt(st.nextToken());

        // key가 번호, value가 포켓폰 이름인 HashMap
        HashMap<Integer, String> pokemonNameMap = new HashMap<Integer, String>();
        // key가 포켓몬 이름, value가 번호인 HashMap
        HashMap<String, Integer> pokemonNumMap = new HashMap<String, Integer>();

        // 포켓몬 도감 HashMap에 입력
        for (int i = 0; i < pokemonNum; i++) {
            String str = br.readLine();
            pokemonNameMap.put(i + 1, str);
            pokemonNumMap.put(str, i + 1);
        }

        for (int i = 0; i < problemNum; i++) {
            String str = br.readLine();

            if(isString(str)) {
                // 포켓몬 이름으로 번호 찾기
                sb.append(pokemonNumMap.get(str));
            } else {
                // 포켓몬 번호로 이름 찾기
                sb.append(pokemonNameMap.get(Integer.parseInt(str)));
            }
            sb.append("\n");
        }

        // 결과 출력
        bw.write(sb.toString());

        bw.flush(); // 남아있는 데이터를 모두 출력시킴
        bw.close(); // 스트림을 닫음
        br.close();

    }

    public static boolean isString(String str) {
        boolean result;

        if (str.charAt(0) >= 'A' && str.charAt(0) <= 'z')
            result = true;
        else
            result = false;

        return result;
    }
}