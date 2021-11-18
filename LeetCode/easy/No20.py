"""
20. 有效的括号
"""


class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        reference_dict = {'(': ')', '[': ']', '{': '}'}
        stack = []
        for char in s:
            if char in reference_dict.keys():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                left = stack.pop()
                if reference_dict.get(left) == char:
                    continue
                else:
                    return False
        return not stack


if __name__ == '__main__':
    solution = Solution()
    print(solution.isValid('{}[]()[(]]'))
