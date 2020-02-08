class Solution:
    def myAtoi(self, str: str) -> int:
        negativeFlag = 1
        isWordOccur = False
        isNumberOccur = False
        isSignOccur = False
        num = 0
        
        for i in range(len(str)):
            if str[i] not in ' +-0123456789':
                break
            elif str[i] == '-':
                if isSignOccur == True or isNumberOccur == True:
                    break
                else:
                    negativeFlag = -1
                    isSignOccur = True
            elif str[i] == '+':
                if isSignOccur == True or isNumberOccur == True:
                    break
                else:
                    negativeFlag = 1
                    isSignOccur = True
            elif str[i] == ' ' and num == 0:
                num = 0
                if isNumberOccur == True or isSignOccur == True:
                    break
            elif str[i] == ' ' and num != 0:
                break
            elif str[i] in '0123456789':
                isNumberOccur = True
                num *= 10
                num += int(str[i])
            else:
                break
                
            # if num > 2**31:
            #     num = 2**31 - 1
            # if num < - 2**31:
            #     num = -2**31
        
        if num * negativeFlag >= 2**31:
            return 2**31 - 1
        if num  * negativeFlag < - 2**31:
            return -2**31
        return num * negativeFlag