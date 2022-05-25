"""
题解3：列表存储，穷举比较
"""
N, m = map(int, input().split(' '))
N = N//10  # 每件物品的价格（都是 10 元的整数倍），为了加快处理速度，先除以10
vpq_list = []
for i in range(m):
    v, p, q = map(int, input().split(' '))
    v = v//10  # 每件物品的价格（都是 10 元的整数倍），为了加快处理速度，先除以10
    vpq_list.append((v, v*p, q, []))
for i, item in enumerate(vpq_list):
    if item[2]:
        vpq_list[item[2] - 1][3].append(i)
vw_list1, vw_list2 = [], []
for i in vpq_list:
    if i[3]:  # 包含附件的主件
        tempList = [(i[0], i[1]), (i[0] + vpq_list[i[3][0]][0], i[1] + vpq_list[i[3][0]][1])]
        vw_list2.append(tempList)
        if len(i[3]) == 2:
            vw_list2[-1].append((i[0] + vpq_list[i[3][1]][0], i[1] + vpq_list[i[3][1]][1]))
            vw_list2[-1].append((i[0] + vpq_list[i[3][0]][0] + vpq_list[i[3][1]][0],
                                 i[1] + vpq_list[i[3][0]][1] + vpq_list[i[3][1]][1]))
    elif not i[2]:  # 不包含附件的主件
        vw_list1.append((i[0], i[1]))
dp = [0 for i in range(N + 1)]
for i in range(1, len(vw_list1) + 1):
    for j in range(N, 0, -1):
        if j >= vw_list1[i - 1][0]:
            dp[j] = max(dp[j], vw_list1[i - 1][1] + dp[j - vw_list1[i - 1][0]])
for i in range(1, len(vw_list2) + 1):
    for j in range(N, 0, -1):
        if j < vw_list2[i - 1][0][0]:
            continue
        if len(vw_list2[i - 1]) == 2:
            if j >= vw_list2[i - 1][1][0]:
                dp[j] = max(dp[j],
                            vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]],
                            vw_list2[i - 1][1][1] + dp[j - vw_list2[i - 1][1][0]])
            else:
                dp[j] = max(dp[j], vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]])
        elif len(vw_list2[i - 1]) == 4:
            if j >= vw_list2[i - 1][3][0]:
                dp[j] = max(dp[j],
                            vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]],
                            vw_list2[i - 1][1][1] + dp[j - vw_list2[i - 1][1][0]],
                            vw_list2[i - 1][2][1] + dp[j - vw_list2[i - 1][2][0]],
                            vw_list2[i - 1][3][1] + dp[j - vw_list2[i - 1][3][0]])
            elif j >= vw_list2[i - 1][1][0] and j >= vw_list2[i - 1][2][0]:
                dp[j] = max(dp[j],
                            vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]],
                            vw_list2[i - 1][1][1] + dp[j - vw_list2[i - 1][1][0]],
                            vw_list2[i - 1][2][1] + dp[j - vw_list2[i - 1][2][0]])
            elif j >= vw_list2[i - 1][2][0]:
                dp[j] = max(dp[j],
                            vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]],
                            vw_list2[i - 1][2][1] + dp[j - vw_list2[i - 1][2][0]])
            elif j >= vw_list2[i - 1][1][0]:
                dp[j] = max(dp[j],
                            vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]],
                            vw_list2[i - 1][1][1] + dp[j - vw_list2[i - 1][1][0]])
            else:
                dp[j] = max(dp[j], vw_list2[i - 1][0][1] + dp[j - vw_list2[i - 1][0][0]])
print(dp[-1]*10)  # 每件物品的价格（都是 10 元的整数倍），由于刚开始为了加快处理速度，先除以10，所以后面需要乘以10
