// https://www.acmicpc.net/problem/10845
// Silver 4 큐

import java.io.*;
import java.util.LinkedList;
import java.util.Queue;

public class BOJ_10845 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringBuilder sb = new StringBuilder();

        Queue<Integer> queue = new LinkedList<Integer>();
        int num = Integer.parseInt(br.readLine());
        int last = -1;

        for (int i = 0; i < num; i++) {
            String[] cmd = br.readLine().split(" ");

            switch (cmd[0]) {
                case "push":
                    last = Integer.parseInt(cmd[1]);
                    queue.offer(last);
                    break;
                case "pop":
                    if (queue.isEmpty()) {
                        sb.append(-1);
                    } else {
                        sb.append(queue.poll());
                    }
                    sb.append("\n");
                    break;
                case "size":
                    sb.append(queue.size());
                    sb.append("\n");
                    break;
                case "empty":
                    sb.append(queue.isEmpty()? 1 : 0);
                    sb.append("\n");
                    break;
                case "front":
                    if (queue.isEmpty()) {
                        sb.append(-1);
                    } else {
                        sb.append(queue.peek());
                    }
                    sb.append("\n");
                    break;
                case "back":
                    if (queue.isEmpty()) {
                        sb.append(-1);
                    } else {
                        sb.append(last);
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