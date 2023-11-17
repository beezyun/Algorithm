// https://www.acmicpc.net/problem/10828
// Silver 4 스택

import java.io.*;
import java.util.Stack;

public class BOJ_10828 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringBuilder sb = new StringBuilder();

        Stack<Integer> stack = new Stack<Integer>();
        int num = Integer.parseInt(br.readLine());

        for (int i = 0; i < num; i++) {
            String[] cmd = br.readLine().split(" ");

            switch (cmd[0]) {
                case "push":
                    stack.push(Integer.parseInt(cmd[1]));
                    break;
                case "pop":
                    if (stack.empty()) {
                        sb.append(-1);
                    } else {
                        sb.append(stack.pop());
                    }
                    sb.append("\n");
                    break;
                case "size":
                    sb.append(stack.size());
                    sb.append("\n");
                    break;
                case "empty":
                    sb.append(stack.empty()? 1 : 0);
                    sb.append("\n");
                    break;
                case "top":
                    if (stack.empty()) {
                        sb.append(-1);
                    } else {
                        sb.append(stack.elementAt(stack.size() - 1));
                    }
                    sb.append("\n");
                    break;
            }
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}