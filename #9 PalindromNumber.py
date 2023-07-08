class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        num = x
        while (num>0):
            rev = rev*10 + num%10
            num = int(num/10)
        if x == rev:
            return True
        else: return False