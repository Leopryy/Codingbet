def centered_average(nums):
    hi = 0
    for i in nums:
        hi += i
    return (hi - max(nums) -min(nums))/(len(nums)-2)