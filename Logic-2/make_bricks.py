def make_bricks(small, big, goal):
    bigneed = goal // 5
    left = goal % 5
    if left == 0:
       return bigneed <= big 
    else:
        smallneed = left/small

