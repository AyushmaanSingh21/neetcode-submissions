class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_str = "".join(char.lower() for char in s if char.isalnum())
       
        n = len(clean_str)
        i = 0
        j = n-1
        while i<j:
            if clean_str[i] != clean_str[j]:
                return False
            i+=1
            j-=1
        return True