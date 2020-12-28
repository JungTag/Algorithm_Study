class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 풀이2 데크 자료형을 이용한 최적화
        strs: Deque = collections.deque()
        
        # 전처리 과정
        for char in s:
            if char.isalnum(): # 영문자, 숫자 여부 판별 
                strs.append(char.lower())
        
        # 팰린드롬 여부 판별
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True