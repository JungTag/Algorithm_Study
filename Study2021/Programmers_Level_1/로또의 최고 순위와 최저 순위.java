package algorithm;

import java.util.HashSet;
import java.util.Set;

public class Prog77484 {
    public static void main(String[] args) {
        Prog77484 s = new Prog77484();
        int[] lottos = {44, 1, 0, 0, 31, 25};
        int[] win_nums = {31, 10, 45, 1, 6, 19};
        int[] answer = s.solution(lottos, win_nums);
        System.out.printf("%d %d", answer[0], answer[1]);
    }
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = new int[2];
        int zero_cnt = 0;
        int correct_cnt = 0;

        Set win_nums_set = new HashSet();
        for (int win_num: win_nums) {
            win_nums_set.add(win_num);
        }

        for (int lotto: lottos) {
            if (lotto == 0) {
                zero_cnt++;
            } else if (win_nums_set.contains((lotto))) {
                correct_cnt++;
            }
        }

        answer[0] = getGrade(zero_cnt + correct_cnt);
        answer[1] = getGrade(correct_cnt);
        return answer;
    }

    int getGrade(int cnt) {
        if (cnt > 1) {
            return 7-cnt;
        } else {
            return 6;
        }
    }
}
