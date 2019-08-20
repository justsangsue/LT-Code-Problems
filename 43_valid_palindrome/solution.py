class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True
        prepro = ""
        for char in s:
            if char.isalpha() or char.isdigit():
                prepro += char.lower()
        return prepro == prepro[::-1]