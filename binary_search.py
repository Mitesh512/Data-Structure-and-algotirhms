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



if __name__ == "__main__":
    nums = [1,2,3,4,5,6,7,8,9]
    target = 7
    target_index = search(nums, target)
    print(target_index)