
def find_common_elements(arr1, arr2):
    common_elements = []
    for item1 in arr1:
        for item2 in arr2:
            if item1 == item2:
                common_elements.append(item1)
    return common_elements

arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(arr1, arr2)
print(common_elements)
