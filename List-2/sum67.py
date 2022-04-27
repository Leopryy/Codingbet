def sum67(nums):
    for i in range(len(nums)):
        if nums[i] == 6:
            nums[i] = 0
            for n in range(i+1,len(nums)):
                stop = nums[n]
                nums[n] = 0
                if stop == 7:
                    break
    return sum(nums)