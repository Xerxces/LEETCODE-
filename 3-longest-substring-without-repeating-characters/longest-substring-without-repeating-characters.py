class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  
        left = 0
        max_len = 0
        for right in range(len(s)):
            char = s[right]
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            char_map[char] = right
            current_len = right - left + 1
            max_len = max(max_len, current_len)
        return max_len