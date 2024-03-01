
def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    # 创建一个二维数组来存储每对字符之间的最长公共子序列长度
    lcs = [[0 for _ in range(n+1)] for _ in range(m+1)]

    # 填充二维数组
    for i in range(1, m+1):
        for j in range(1, n+1):
            if str1[i-1] == str2[j-1]:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    # 从二维数组中回溯出最长公共子序列
    index = lcs[m][n]
    lcs_sequence = [""] * (index+1)
    lcs_sequence[index] = ""
    i = m
    j = n
    while i > 0 and j > 0:
        if str1[i-1] == str2[j-1]:
            lcs_sequence[index-1] = str1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif lcs[i-1][j] >= lcs[i][j-1]:
            i -= 1
        else:
            j -= 1

    return "".join(lcs_sequence)
