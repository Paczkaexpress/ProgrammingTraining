class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_res = ""
        flagSpecial = False
        
        if numRows == 1:
            return s
        
        for i in range(numRows):
            j = 0
            k = 0
            flagSpecial = False
            while k < len(s):
                if i == 0 or i == numRows - 1:
                    k = i + 2*j*(numRows - 1)
                else:
                    if flagSpecial == True:
                        j -= 1
                        k = 2*j*(numRows - 1) + 2*numRows - 2 - i
                        flagSpecial = False

                    else:
                        k = i + 2*j*(numRows - 1)
                        flagSpecial = True

                # print(k)
                if k >= len(s):
                    break
                s_res += s[k]

                # print(s_res)
                
                j += 1
                
        return s_res