def array123(nums):
    for i in range(len(nums)):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False