class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        acceptedCharacters = "0123456789e+-."
        
        newS = ""
        
        #need to delete leading and trailing spaces
        for i in range(len(s)):
            if s[i] != ' ':
                newS = s[i:]
                break
        print(s)        
        s = newS
        for i in range(len(s)-1,-1, -1):
            if s[i] != ' ':
                newS = s[:i+1]
                break  
        s = newS
        print(s)
        if len(s) == 0:
            return False
        print("length > 0")
        if len(s) == 1 and s in "0123456789":
            return True
        elif len(s) == 1 and s not in "0123456789":
            return False
        print(s)
        #chacking if all characters are valid:
        for c in s:
            print(c)
            if c not in acceptedCharacters:
                print("wtf")
                return False
            
        # print("All characters accepted")
        if s.count('.') > 1:
            return False
        
        if s.count('+') > 2:
            return False
        
        if s.count('-') > 2:
            return False
        
        if s.count('e') > 1:
            return False
        elif s.count('e') == 1:
            arr = s.split('e')
            
            if len(arr[0]) == 0 or len(arr[1]) == 0:
                return False
            
            numberFlag = False
            for c in arr[0]:
                if c in "0123456789":
                    numberFlag = True
            if numberFlag == False:
                return False
            numberFlag = False
            for c in arr[1]:
                if c in "0123456789":
                    numberFlag = True
            if numberFlag == False:
                return False
                
            if '+'in arr[0][1:]:
                return False
            if '-'in arr[0][1:]:
                return False
            if '+'in arr[1][1:]:
                return False
            if '-'in arr[1][1:]:
                return False
            if '.' in arr[1]:
                return False
        else:
            if '-' in s[1:]:
                return False
            if '+' in s[1:]:
                return False
            numberFlag = False
            for c in s:
                if c in "1234567890":
                    numberFlag = True
            if numberFlag == False:
                return False
                
            
        return True
        
        