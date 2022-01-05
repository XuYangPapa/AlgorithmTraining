"""
3. 无重复字符的最长子串
"""


class Solution:
    def lengthOfLongestSubstring_set(self, s: str) -> int:
        """
        滑动窗口（low指针逐步右移，效率较低）
        """
        if len(s) <= 1:
            return len(s)
        low, high = 0, 1
        letter_set = set()
        letter_set.add(s[0])
        max_len = 1
        while high < len(s):
            if s[high] not in letter_set:
                letter_set.add(s[high])
                max_len = max(max_len, len(letter_set))
                high += 1
            else:
                letter_set.remove(s[low])
                low += 1
        return max_len

    def lengthOfLongestSubstring_map(self, s: str) -> int:
        """
        滑动窗口（low指针利用map记录的下标直接跳转，max_len通过high和low确定，不再通过len(map)确定）
        """
        if len(s) <= 1:
            return len(s)
        low, high = 0, 1
        letter_map = {s[0]: 0}
        max_len = 1
        while high < len(s):
            if s[high] in letter_map.keys():
                """
                如果low>letter_map[s[high]]+1，意味着出现s[high]的位置已经在当前考虑的字符串之前了，可以忽略。
                如果下方写成:low = letter_map[s[high]]+1，那么只需将上方的if添加一个条件：low<=letter_map[s[high]]即可。
                """
                low = max(letter_map[s[high]] + 1, low)
            max_len = max(max_len, high - low + 1)
            letter_map[s[high]] = high
            high += 1
        return max_len


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring_map('abba'))
