def binarySearch(arr, number):
    left,right = 0, (len(arr)) - 1
    arr.sort()
    while left <= right:
        middle = (left + right)//2
        print(middle)
        if arr[middle] == number:
            return middle
        elif arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return "Not Found"

arr = [i for i in range(0,101)]
print(binarySearch(arr,-5))


def binarySearch(arr, number, left=0, right=None):
    if right is None:
        right = len(arr)-1

    if left > right:
        return "Not Found"
    
    arr.sort()
    if left <= right:
        middle = (left + right) // 2
        if arr[middle] == number:
            return middle
        elif arr[middle] < number:
            return binarySearch(arr, number, middle + 1, right)
        else:
            return binarySearch(arr, number, left, middle - 1)
    else:
        return "Not Found"


arr = [0, 0, 0, 0, 1, 1, 1]
print(binarySearch(arr,1))
