from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
        word_len = len(words[0])
        total_words = len(words)
        total_len = word_len * total_words
        s_len = len(s)
        if s_len < total_len:
            return []
        word_count = Counter(words)
        res = []
        for i in range(word_len):
            left = i
            right = i
            seen = Counter()
            count = 0
            while right + word_len <= s_len:
                word = s[right : right + word_len]
                right += word_len
                if word in word_count:
                    seen[word] += 1
                    count += 1
                    while seen[word] > word_count[word]:
                        left_word = s[left : left + word_len]
                        seen[left_word] -= 1
                        count -= 1
                        left += word_len
                    if count == total_words:
                        res.append(left)
                else:
                    seen.clear()
                    count = 0
                    left = right

        return res