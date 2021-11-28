"""
53. 最大子序和
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        动态规划思路。
        可以维护一个dp数组，但是因为每次计算下标i的最大和时我们只关心i-1的最大和的情况，
        所以可以使用一个dp_pre来代替dp数组，一个max_sum维护最大和，以此降低空间复杂度。
        """
        dp_pre = nums[0]
        max_sum = dp_pre
        for i in range(1, len(nums)):
            dp_pre = max(dp_pre + nums[i], nums[i])
            max_sum = max(dp_pre, max_sum)
        return max_sum


if __name__ == '__main__':
    solution = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solution.maxSubArray(nums))
