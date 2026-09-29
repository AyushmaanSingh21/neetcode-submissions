class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        max_freq = 0
        
        l = 0
        for r in range(len(s)):
            # Add the current character to the frequency map
            count[s[r]] = 1 + count.get(s[r], 0)
            
            # Track the most frequent character in the current window
            max_freq = max(max_freq, count[s[r]])
            
            # Window length is (r - l + 1)
            # If remaining characters to replace exceed k, shrink window
            if (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            # Update the maximum valid window size found so far
            res = max(res, r - l + 1)
            
        return res
