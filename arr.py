# def binarySearch(arr, number):
#     left,right = 0, (len(arr)) - 1
#     arr.sort()
#     while left <= right:
#         middle = (left + right)//2
#         print(middle)
#         if arr[middle] == number:
#             return middle
#         elif arr[middle] < number:
#             left = middle + 1
#         else:
#             right = middle - 1
#     return "Not Found"

# arr = [i for i in range(0,101)]
# print(binarySearch(arr,-5))


# def binarySearch(arr, number, left=0, right=None):
#     if right is None:
#         right = len(arr)-1

#     if left > right:
#         return "Not Found"
    
#     arr.sort()
#     if left <= right:
#         middle = (left + right) // 2
#         if arr[middle] == number:
#             return middle
#         elif arr[middle] < number:
#             return binarySearch(arr, number, middle + 1, right)
#         else:
#             return binarySearch(arr, number, left, middle - 1)
#     else:
#         return "Not Found"



def countOccurrences(arr, number):
    left = 0
    right = len(arr) - 1

    first_occurrence = findFirstOccurrence(arr, number, left, right)
    last_occurrence = findLastOccurrence(arr, number, left, right)

    if first_occurrence != -1:
        return last_occurrence - first_occurrence + 1
    else:
        return 0

def findFirstOccurrence(arr, number, left, right):
    first_occurrence = -1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == number:
            first_occurrence = middle
            right = middle - 1
        elif arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return first_occurrence

def findLastOccurrence(arr, number, left, right):
    last_occurrence = -1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == number:
            last_occurrence = middle
            left = middle + 1
        elif arr[middle] < number:
            left = middle + 1
        else:
            right = middle - 1
    return last_occurrence

arr = [1, 2, 2, 3, 3, 3, 4, 5]
number = 3

count = countOccurrences(arr, number)
print(f"The number {number} appears {count} times in the list.")


arr = [0, 0, 0, 0, 1, 1, 1,1]
# print(binarySearch(arr,0))


