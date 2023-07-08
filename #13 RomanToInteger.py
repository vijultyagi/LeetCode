class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        prev = 1001
        result = 0
        
        for char in s:
            if dic[char] > prev:
                result -= 2 * prev
            result += dic[char]
            prev = dic[char]
            
        return result