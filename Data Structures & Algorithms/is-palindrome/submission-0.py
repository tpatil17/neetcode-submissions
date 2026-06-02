class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        def AlphaNumeric(s):
            print(ord(s))
            if ((65 <= ord(s) <= 90) 
            or (48 <= ord(s) <= 57) 
            or (97 <= ord(s) <= 122)):
                return True
            else:
                return False


        arr = []

        for i in s:

            if AlphaNumeric(i):
                arr.append(i.lower())
        
        print(arr)
        if arr[::-1] == arr:
            return True
        else:
            return False

