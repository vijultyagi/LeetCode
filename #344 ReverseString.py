# Space Complexity O(1)
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0
        j = len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            j -= 1
            i += 1