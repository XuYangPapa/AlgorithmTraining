class No1(object):

    def twoSum_sort(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        排序以后从两头开始查找
        时间复杂度：O(nlogn), 空间复杂度：O(n)
        """
        sorted_nums = sorted(nums)
        low, high = 0, len(nums) - 1
        while low < high:
            res = sorted_nums[low] + sorted_nums[high]
            if res == target:
                break
            elif res < target:
                low += 1
            else:
                high -= 1
        first = nums.index(sorted_nums[low])
        second = nums.index(sorted_nums[high])
        if first == second:
            second = nums.index(sorted_nums[high], first + 1, len(nums))
        return first, second

    def twoSum_hashtable(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        建立hash表用于查找前面访问过的元素
        时间复杂度：O(n), 空间复杂度：O(n)
        """
        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
        return []


if __name__ == '__main__':
    no1 = No1()
    nums = [3, 3]
    print(no1.twoSum_hashtable(nums, 6))
