"""
17. 电话号码的字母组合
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        暴力走DFS搜索遍历所有情况（这种需列出所有情况的问题，一般没有太多捷径，只能全遍历）
        :param digits:
        :return:
        """
        digit_dict = {'2': ['a', 'b', 'c'],
                      '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'],
                      '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'],
                      '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'],
                      '9': ['w', 'x', 'y', 'z']
                      }
        res_list = list()
        if not digits:
            return res_list

        def dfs_search(index, cur_str):
            if index == len(digits):
                res_list.append(cur_str)
            else:
                for letter in digit_dict[digits[index]]:
                    next_str = cur_str + letter
                    dfs_search(index + 1, next_str)
        dfs_search(0, '')
        return res_list


if __name__ == '__main__':
    solution = Solution()
    digits = "23"
    print(solution.letterCombinations(digits))
