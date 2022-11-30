def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1
 
arr = [7,10,12,14,16,20,29,37]
target = 14
target1 = 29
# Function call
result = binary_search(arr, target)

result1 = binary_search(arr, target1)
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

if result != -1:
    print("Element is present at index", str(result1))
else:
    print("Element is not present in array")
