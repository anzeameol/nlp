
def find_common_elements(arr1, arr2):
    common_elements = []
    for num1 in arr1:
        for num2 in arr2:
            if num1 == num2 and num1 not in common_elements:
                common_elements.append(num1)
    return common_elements

# 测试代码
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
print(find_common_elements(arr1, arr2))
