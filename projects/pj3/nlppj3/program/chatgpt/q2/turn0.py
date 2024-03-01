
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)
    # 创建一个二维数组来保存最长公共子序列的长度
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # 动态规划求解最长公共子序列的长度
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # 回溯构造最长公共子序列
    lcs_length = dp[m][n]
    lcs = [''] * lcs_length
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs[lcs_length - 1] = str1[i - 1]
            i -= 1
            j -= 1
            lcs_length -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(lcs)
