



# a,b,c取值范围
# range(1001)

import time

start_time=time.time()

for a in range(1001): # 1001 问题规模
    # 每个a的取值
    # 正对每个a的取值，b都有1001中可能性
    for b in range(1001): # 1001
        # a,b的一种可能组合，c也有1001种可能性
        for c in range(1001): # 1001
            # a,b,c的某一种可能性
            # 符合自然数的已知条件
            if a+b+c==1000 and a**2+b**2==c**2: # 9
                print(a,b,c)

end_time = time.time()


print("total cost:", end_time-start_time)

# 绝对时间描述算法的好坏： 不同的的机器硬件和软件的环境都不一样,绝对时间不靠谱
# total cost: 244.53107380867004


# 绝对时间 = 算法的运行步骤（确定的）* 每一步运行的耗时（和机器硬件有关，不确定的）
# 用 算法的运行步骤（确定的） 来描述算法优劣
# y = N^3 * 9
# 时间复杂度：O(N^3)

