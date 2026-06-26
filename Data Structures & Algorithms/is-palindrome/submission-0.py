class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = s

        n = len(char)
        i = 0
        j = n - 1

        while i < j:

            while i < j and not char[i].isalnum():
                i += 1

            while i < j and not char[j].isalnum():
                j -= 1

            if char[i].lower() != char[j].lower():
                return False

            i += 1
            j -= 1

        return True