"""
35. 搜索插入位置
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        二分查找
        有序数组中找到返回下标和找不到返回插入位置可以合并为在一个有序数组中找第一个大于等于target的下标
        注意整数溢出问题
        """
        if len(nums) == 0:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            # 避免整数溢出
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 7))
