
# Best time to sell stock
def maxProfit(prices):
    # Brute Force Approach:
    # profit = 0
    # for i in range(len(prices)):
    #     for j in range(i,len(prices)):
    #         if prices[j]>prices[i]:
    #             new_sum = prices[j] - prices[i]
    #             if new_sum > profit:
    #                 profit = new_sum
    # return profit

    # Better Approach
    min_price = 10**6
    profit = 0
    for p in prices:
        if p < min_price:
            min_price = p
        if p > min_price:
            if (p-min_price) > profit:
                profit = p - min_price

    return profit


# Find Duplicate in array:
def find_duplicate(arr):
    # Brute Force Approach:
    # for i in range(len(arr)):
    # 	for j in range(i+1,len(arr)):
    # 		if arr[i] == arr[j]:
    # 			return True
    # return False

    # Better Approach
    # arr = sorted(arr)
    # for i in range(len(arr)-1):
    # 	if arr[i] == arr[i+1]:
    # 		return True
    # return False

    # Optimal
    ele_count_dict = {}
    for i in arr:
        if i in ele_count_dict.keys():
            ele_count_dict[i] +=1
        else:
            ele_count_dict[i] = 1
    if len(arr) != len(ele_count_dict):
        return True
    else:
        return False
    



# find the second larges element in the array
def find_second_largest(arr):
    # sort the array Brute Force TC O(nlogn) + O(N)
    # arr = sorted(arr)

    # for i in range(len(arr)-2,-1,-1):
    #     if arr[i] < arr[len(arr)-1]:
    #         return arr[i]

    # Better Approach: TC O(n)
    larget_element = arr[0]
    second_largest = -1e6

    for i in range(1,len(arr)):
        if arr[i]>larget_element:
            second_largest = larget_element
            larget_element = arr[i]
        elif arr[i] == larget_element:
            continue
        elif (arr[i] > second_largest) and (arr[i]<larget_element):
            second_largest = arr[i]

    return second_largest


def push_zeros_to_right(arr):
    optimal_flag = False
    # Brute Force Approach TC O(n) SC O(n)
    if optimal_flag:
        non_zero_arr = []
        total_zeros = 0
        for i in range(len(arr)):
            if arr[i] !=0:
                non_zero_arr.append(arr[i])
            else:
                total_zeros +=1
        return non_zero_arr + [0] * total_zeros

    
    # Optimal Solution TC O(n) --> x + (n-x) , SC O(1)  
    # find j where 0 is found 
    j = -1
    for i in range(len(arr)):
        if arr[i]==0:
            j = i
            break
    
    for i in range(j+1,len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1
    return arr


def containsDuplicate(nums):
    # Brute Force Approach

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:

                return "true"
    return "false"

        
if __name__ == "__main__":
    arr = [1,2,3,4]
    result = containsDuplicate(arr)
    print(result)

