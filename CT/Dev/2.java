import java.util.Stack;

class Solution {
    public int[] solution(int[] deposit) {
        Stack<Integer> history = new Stack<>();
        
        for (int money:deposit) {
            if (money > 0) {
                history.push(money);
            } else {
                int sum = 0; // 현재까지 출금한 금액
                int abs = -(money);
                while (sum < abs) {
                    int diff = abs - sum;
                    int last = history.pop();
                    if (last > diff) {
                        history.push(last - diff);
                    }
                    sum += last;
                }
            }
        }
        
        int[] answer = history.stream().mapToInt(i->i).toArray();
        
        return answer;
    }
}