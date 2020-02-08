class Solution:
    def longestPalindrome(self, s: str) -> str:
        lps = ""
        S = ""
        
        for st in range(len(s)):
            S = s[st]
            
            if len(S) > len(lps):
                lps = S
                
            for i in range(1,len(s)):
                if st - i < 0:
                    break
                if st + i > len(s)-1:
                    break
                
                if s[st+i] == s[st-i]:
                    S = s[st-i] + S + s[st+i]
                    # print(S)
                if len(S) > len(lps):
                    lps = S
                    # print(S)
                if s[st+i] != s[st-i]:
                    break
                        
        for st in range(len(s)-1):
            if s[st] != s[st+1]:
                continue
                
            S = s[st]
            S += s[st+1]
                
            if len(S) > len(lps):
                lps = S
                
            for i in range(1,len(s)-1):
                if st - i < 0:
                    break
                if st + i + 1> len(s)-1:
                    break
                
                if s[st+i+1] == s[st-i]:
                    S = s[st-i] + S + s[st+i+1]
                if len(S) > len(lps):
                    lps = S
                    # print(S)
                if s[st+i+1] != s[st-i]:
                    break
        return lps