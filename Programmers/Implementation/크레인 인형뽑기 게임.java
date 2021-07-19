// https://programmers.co.kr/learn/courses/30/lessons/64061?language=java
import java.util.Stack;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        int LEN = board.length;
        
        Stack<Integer> basket = new Stack<>();
        basket.push(-1);
        
        for (int num:moves) {
            int c = num-1;
            for (int i=0; i<LEN; i++) {
                if (board[i][c] != 0) {
                    int value = board[i][c];
                    if (basket.peek() == value) {
                        basket.pop();
                        answer += 2;
                    } else {
                        basket.push(value);    
                    }
                    board[i][c] = 0;
                    break;
                }
            }
        }
        return answer;
    }
    
}