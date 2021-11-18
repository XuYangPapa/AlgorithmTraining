"""
28. 实现strStr()
"""


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        双指针构建滑动窗口
        """
        if len(needle) == 0:
            return 0
        if len(haystack) == 0 or len(haystack) < len(needle):
            return -1
        front, back = 0, len(needle)
        while back <= len(haystack):
            sub_str = haystack[front: back: 1]
            if sub_str == needle:
                return front
            else:
                front += 1
                back += 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.strStr('hello', 'll'))
