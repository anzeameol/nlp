
def binary_search(arr, target):
    """
    Implement a binary search algorithm to find a specific element in a sorted array.
    
    Parameters:
    arr (list): The sorted array in which to search for the target element.
    target (int): The element we want to find in the array.
    
    Returns:
    int: The index of the target element in the array, or -1 if it is not found.
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
