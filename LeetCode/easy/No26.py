"""
26. 删除有序数组中的重复项
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        不需要删除元素，只需要将重复的元素移动至列表的右侧，删除元素的话耗时较高。
        注意对原本就不重复列表的优化
        """
        if len(nums) <= 1:
            return len(nums)
        index1, index2 = 0, 1
        while index2 < len(nums):
            if nums[index1] != nums[index2]:
                if index1 + 1 < index2:
                    nums[index1+1] = nums[index2]
                index1 += 1
            index2 += 1
        return index1 + 1


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    size = solution.removeDuplicates(nums)
    for i in range(size):
        print(nums[i])
