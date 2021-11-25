import random


def bi_search_basic(nums, target):
    """
    无重复、升序列表
    存在时返回target所在位置，不存在时返回元素应该被插入位置（或-1）
    """
    low, high = 0, len(nums) - 1  # 双闭区间
    while low <= high:  # 双闭区间的退出条件
        mid = low + (high - low) // 2  # 下中位数
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low  # 也可为-1


def bi_search_findLower_closeInterval(nums, target):
    """
    有重复、升序列表（适用于无重复的情况）
    存在时返回target所在位置，不存在时返回元素应该被插入位置
    搜索空间采用双闭
    """
    low, high = 0, len(nums) - 1  # 双闭区间
    while low <= high:  # 双闭区间退出条件
        mid = low + (high - low) // 2  # 下中位数
        if nums[mid] == target:
            high = mid - 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return low


def bi_search_findLower_openInterval(nums, target):
    """
    有重复、升序列表（适用于无重复的情况）
    存在时返回target所在位置，不存在时返回元素应该被插入位置
    搜索空间采用前闭后开
    """
    low, high = 0, len(nums)    # 前闭后开区间
    while low < high:   # 前闭后开区间的退出条件
        mid = low + (high - low) // 2   # 下中位数
        if nums[mid] == target:
            high = mid
        elif nums[mid] > target:
            high = mid
        else:
            low = mid + 1
    return low


def generate_test():
    for i in range(10):
        nums = []
        for j in range(20):
            nums.append(random.randint(0, 10))
        nums.sort()
        target = random.randint(1, 10)
        actual_index = -1
        for index, num in enumerate(nums):
            if num >= target:
                actual_index = index
                break
        my_index = bi_search_findLower_closeInterval(nums, target)
        print(nums)
        print(target)
        print(actual_index)
        print(my_index)
        print('-------')


if __name__ == '__main__':
    # generate_test()

    nums1 = [1, 3, 5, 7, 10]
    target1 = -1
    nums2 = [1, 3, 3, 3, 10]
    target2 = 11
    print(bi_search_findLower_openInterval(nums2, target2))
