



# a,b,c取值范围
# range(1001)

import time

start_time=time.time()


for a in range(1001): # 1001
    # 每个a的取值
    # 正对每个a的取值，b都有1001中可能性
    for b in range(1001): # 1001
        # a,b的一种可能组合，c也有1001种可能性
        # 确定c的值
        c = 1000 - a - b # 3
        # 到此位置又得到了a，b，c的一种组合
        # 符合a+b+c=1000,自然数
        if a**2+b**2 == c**2: # 5
            print(a,b,c)


end_time = time.time()

print("total cost:", end_time-start_time)


# total cost: 1.657470941543579


# y = N^2 * 8
# 时间复杂度：O(N^2)