"""
27. 移除元素
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        前后双指针遍历
        """
        if len(nums) == 0:
            return 0
        save, remove = 0, len(nums) - 1
        while save <= remove:
            if nums[save] == val:
                nums[save] = nums[remove]
                remove -= 1
            else:
                save += 1
        return remove + 1 if remove >= 0 else 0


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    size = solution.removeElement(nums, 2)
    for i in range(size):
        print(nums[i])
