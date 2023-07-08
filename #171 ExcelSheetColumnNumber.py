class Solution:
    # Using ASCII, and taking base number as 26
    # Space Complexity O(1)
    def titleToNumber(self, columnTitle: str) -> int:
        j = 0
        result = 0

        for char in reversed(columnTitle):
            result += (ord(char) - 64) * 26**j
            j += 1
        return result