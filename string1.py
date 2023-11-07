class NotRotatedError(BaseException):
    def __init__(self, message):
        super().__init__(message)

arr = [5,6,7,0,1,2,3,4]
def rotatedBinarySearh(arr, target):
    left, right = 0, len(arr) - 1    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid]==target:
            return mid
        
        if arr[left]<=arr[mid]:
            if arr[left] <= target <arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[right]>arr[mid]:
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    raise NotRotatedError("Given array is not rotated or value is not found")

#print(rotatedBinarySearh(arr,4))

arr = [1,3,5,6,8,9,19]

def binarySeachInsert(arr,target):
    left, right = 0, len(arr) - 1   
    while left <= right:
        
        mid = (left + right) // 2
        if arr[mid]==target:
            return mid
        
        if arr[mid]<target:
            left = mid + 1

        elif arr[mid]>target:
            right = mid -1
    return left
        


a = binarySeachInsert(arr,2)
print(a)
print(__name__)




