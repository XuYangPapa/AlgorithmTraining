"""
11. 盛最多水的容器
"""
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        头尾指针，小的先向中间移动
        """
        low, high = 0, len(height) - 1
        max_area = -1
        while low < high:
            max_area = max(max_area, min(height[low], height[high]) * (high - low))
            if height[low] < height[high]:
                low += 1
            else:
                high -= 1
        return max_area

if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea([1,8,6,2,5,4,8,3,7]))