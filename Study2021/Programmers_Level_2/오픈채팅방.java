// https://programmers.co.kr/learn/courses/30/lessons/42888

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

class Solution {
    public String[] solution(String[] record) {
        List<String> answerList = new ArrayList<String>();
        HashMap<String, String> userMap = new HashMap<String, String>();

        for (String str : record) {
            String[] splittedStr = str.split(" ");
            String action = splittedStr[0];
            String userId = splittedStr[1];

            if (action.equals("Enter") || action.equals("Change")) {
                String userName = splittedStr[2];
                userMap.put(userId, userName);
            }
        }

        for (String str : record) {
            String[] splittedStr = str.split(" ");
            String action = splittedStr[0];
            String userId = splittedStr[1];

            if (action.equals("Enter") || action.equals("Leave")) {
                answerList.add(getFormattedStr(action, userMap.get(userId)));
            }
        }

        String[] answer = answerList.toArray(new String[answerList.size()]);
        
        return answer;
    }

    private String getFormattedStr(String action, String userName) {
        StringBuilder sb = new StringBuilder(userName);
        if (action.equals("Enter")) {
            return sb.append("님이 들어왔습니다.").toString();
        }
        return sb.append("님이 나갔습니다.").toString();
    }
}