
def find_common_elements(arr1, arr2):
    set1 = set(arr1)
    set2 = set(arr2)

    common_elements = list(set1 & set2)

    return common_elements

# 测试
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]

print(find_common_elements(arr1, arr2))  # 输出: [4, 5]
