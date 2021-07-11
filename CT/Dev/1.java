class Solution {
    public int solution(int[] d, int m) {
        int answer = 0;
        int boxes = 1;
        
        for (int num:d) {
            answer += 1;
            if (num >= boxes) {
                m -= boxes;
                boxes *= 2;
            } else {
                boxes = 1;
            }
            if (m <= 0) {
                break;
            }
        }
        if (m > 0) {
            answer = -1;
        }
        return answer;
    }
}