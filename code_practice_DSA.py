# Write a program to Find k closest elements to a given value

# Input: K = 4, X = 35

# arr[] = {12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56}

# Output: 30 39 42 45


def find_closest_elements(arr, k, x):
    # Sort the array based on the absolute difference from x
    arr.sort(key=lambda num: abs(num - x))
    
    # Filter out the target value x and take k elements
    result = [num for num in arr if num != x][:k]
    
    # Sort the result to maintain the original order
    result.sort()
    
    return result


print(
    find_closest_elements([12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56], 4, 35)
)
