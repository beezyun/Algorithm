// https://www.acmicpc.net/problem/2750
// Bronze 2 수 정렬하기

import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class BOJ_2750 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int num = Integer.parseInt(br.readLine());
        ArrayList<Integer> arr = new ArrayList<Integer>();

        for (int i = 0; i < num; i++) {
            arr.add(Integer.parseInt(br.readLine()));
        }

        // 오름차순 정렬
        Collections.sort(arr);
        for (int i = 0; i < arr.size(); i++) {
            bw.write(arr.get(i).toString());
            if (i != arr.size() - 1) {
                bw.newLine();
            }
        }

        bw.flush();
        bw.close();
    }
}