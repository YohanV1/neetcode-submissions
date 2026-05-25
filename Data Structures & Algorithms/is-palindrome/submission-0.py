class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for letter in s:
            if letter.isalnum():
                s_new += letter.lower()
        return s_new==s_new[::-1]
        