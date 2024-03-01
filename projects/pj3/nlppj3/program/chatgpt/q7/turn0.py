
def find_common_elements(array1, array2):
    set1 = set(array1)
    set2 = set(array2)
    common_elements = set1.intersection(set2)
    return list(common_elements)

# 测试示例
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(array1, array2)
print(common_elements)
