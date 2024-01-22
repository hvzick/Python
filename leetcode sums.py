def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] + nums[j] == target:
                x = nums.index(nums[i])
                y = nums.index(nums[j])
                print(x, y)
            j = j + 1
        i = i + 1

    return x, y


nums1 = [3, 3]
target1 = 6
twoSum(nums1, target1)
