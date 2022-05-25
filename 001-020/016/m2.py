"""
题解2：字典存储，穷举比较
"""
N, m = map(int, input().split())
N = N // 10
main_parts = {}
accessories = {}
for i in range(1, m+1):
    v, p, q = map(int, input().split())
    v = v // 10
    if q:
        accessories.update({i: (v, v*p, q)})
    else:
        main_parts.update({i: (v, v*p, [])})
for i, value in accessories.items():
    main_parts[accessories[i][2]][2].append((accessories[i][0], accessories[i][1]))
dp = [0 for i in range(N + 1)]
for k, main_part in main_parts.items():
    _accessories = main_part[2]
    for j in range(N, 0, -1):
        if j < main_part[0]:
            dp[j] = dp[j]
        elif len(_accessories) == 0:
            dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]])
        elif len(_accessories) == 1:
            if j >= main_part[0] + _accessories[0][0]:
                dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]],
                            main_part[1] + _accessories[0][1] + dp[j - main_part[0] -
                                                                   _accessories[0][0]])
            else:
                dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]])
        elif len(_accessories) == 2:
            if j >= main_part[0] + _accessories[0][0] + _accessories[1][0]:
                dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]],
                            main_part[1] + _accessories[0][1] + dp[j - main_part[0] -
                                                                   _accessories[0][0]],
                            main_part[1] + _accessories[0][1] + _accessories[1][1] + dp[
                                j - main_part[0] - _accessories[0][0] - _accessories[1][0]])
            elif j >= main_part[0] + _accessories[0][0]:
                dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]],
                            main_part[1] + _accessories[0][1] + dp[j - main_part[0] -
                                                                   _accessories[0][0]])
            elif j >= main_part[0] + _accessories[1][0]:
                dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]],
                            main_part[1] + _accessories[1][1] + dp[j - main_part[0] -
                                                                   _accessories[1][0]])
            else:
                dp[j] = max(dp[j], main_part[1] + dp[j - main_part[0]])
print(dp[-1]*10)
