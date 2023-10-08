def recursive_binary_seach(nums,low,high,target):
    
    if low > high:
        return -1
    mid = (low + high) //2
    print(low,high,mid)
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return recursive_binary_seach(nums,mid+1,high,target)
    
    return recursive_binary_seach(nums,low,mid-1,target)


def search(nums: [int], target: int):
    # Write your code here.
    """
    we create two pointers and seach like a dictionary
    
    """
    # low = 0
    # high = len(nums) -1
    
    # while (low <= high):
    #     mid = (low+high)//2
    #     if nums[mid] == target:
    #         return mid
    #     elif nums[mid] < target:
    #         low = mid +1
    #     else:
    #         high = mid -1
    # return -1

    # Recursive implimentaiton
    low = 0
    high = len(nums) -1
    return recursive_binary_seach(nums,low,high,target)

def rec_lb(arr,low,high,x):
    if low > high:
        return low
    mid = (low + high) //2

    if arr[mid] >= x:
        return rec_lb(arr,low,mid-1,x)
    return rec_lb(arr,mid+1,high,x)


def lowerBound(arr: [int], n: int, x: int) -> int:
    # Write your code here
    """
    [1,2,3,4,5,6,7,8,9,10], x = 8
    lower bound >= x
    initially we define the lower bound as n the last element lb = n
    define low = 0 and high = n -1
    base condition
    while (low <= high):
        mid = (low + high) /2
        if arr[mid] >= x:
            lb = mid
            high= mid-1

        elif arr[mid] < x:
            low = mid + 1

    """
    # Brute Force Approach: TC O(n)
    # lb = n
    # for i in range(n):
    #     if arr[i] >= x:
    #         lb = i
    #         return lb
    # return lb

    # OPtimal Approach is Binary Search
    # lb = n
    # low = 0
    # high = n-1
    # while (low <= high):
    #     mid = (low + high) //2
    #     if arr[mid] >= x:
    #         lb = mid
    #         high= mid-1

    #     elif arr[mid] < x:
    #         low = mid + 1
    # return lb

    # Recursive approach
    low = 0
    high = n-1
    return rec_lb(arr,low,high,x)

 
def searchin_rotated_sorted_array (arr, n, k):

	# Write your code here

	# Brute Force Approach
	# for i in range(n):
	# 	if arr[i] == k:
	# 		return i
	# return -1

	# Binary Search Approach
	# [6,7,8,9,1,2,3,4,5] k =5
	low = 0
	high = n-1

	while(low<=high):
		mid = (low+high)//2
		if arr[mid] == k:
			return mid
		# now we need to identify the sorted array and then check whether target is there or not
		if arr[low] <= arr[mid]:
			if ((arr[low] <= k) and (k<arr[mid])):
				high = mid -1
			else:
				low = mid +1
		
		else:
			if ((arr[high]>= k) and (k > arr[mid])):
				low = mid +1
			else:
				high = mid -1
	return -1



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    target = 7
    target_index = search(nums, target)
    print(target_index)