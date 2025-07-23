# Find 1 Missing Element in a list of n Natural Numbers
def find_missing_element(arr,n):
    """
    arr = [2,4,1,5]
    n=5
    missing_element = find_missing_element(arr,n)
    print(missing_element)
    """

    # Brute Force Approach: TC O(nXn) SC O(1)
    # for i in range(1,n+1):
    #     found_flag = 0
    #     for j in range(len(arr)):
    #         if i == arr[j]:
    #             found_flag = 1
    #             break
    #     if found_flag == 0:
    #         return i
    # return -1

    # Better Approach We can use Hashing: TC O(2n),  SC O(n)
    # arr_hash = [0] * (n + 1)
    # for i in arr:
    #     arr_hash[i] = 1
    # for i in range(1,n+1):
    #     if arr_hash[i] == 0:
    #         return i
    # return -1

    # Further Optimal Solution TC O(n), SC O(1) ----> There's a probem if the arr size is 10^6 --> sum will be 10^6 X 10^6 /2 --> 10^12 excceds memroy space
    ele_sum = 0
    for i in arr:
        ele_sum += i
    if ele_sum == (n*(n+1)/2):
        return -1
    else:
        return int((n*(n+1)/2) - ele_sum)


# find the element which appears only once all other are twice
def find_once_ele(arr):
    """
    arr = [1,2,3,4,5,1,3,4,2]
    once_ele = find_once_ele(arr)
    print(once_ele)
    
    """
    # TC O(2n), SC O(n/2)
    # arr_dict = {}
    # for i in arr:
    #     if arr_dict.get(i):
    #         arr_dict[i] += 1
    #     else:
    #         arr_dict[i] = 1
    # for k in arr_dict.keys():
    #     if arr_dict[k] ==1:
    #         return k
        
    # Optimal
    xor_sum = 0
    for i in arr:
        xor_sum = xor_sum ^ i
    if xor_sum == 0:
        return -1
    else:
        return xor_sum


def find_subarray(arr):

    """
    what will be my brute force approach:
    get all single elements.
    [1,2,3,5]

    1
    12
    123
    1235

    2
    23
    235

    3
    35

    5
    
    """
    
    # Brute Force Approach:
    all_sub_arrays = []
    for i in range(len(arr)):
        sub_arr = []
        for j in range(i,len(arr)):
            sub_arr = sub_arr.copy()
            sub_arr.append(arr[j])
            all_sub_arrays.append(sub_arr)
        sub_arr = []
    return all_sub_arrays
            


def longest_sub_array_with_k_sum(arr, k):
    # Brute Force Approach:
    all_sub_arrays = []
    sub_array_with_k_sum_dict = {}
    for i in range(len(arr)):
        sub_arr = []
        for j in range(i,len(arr)):
            sub_arr = sub_arr.copy()
            sub_arr.append(arr[j])
            if sum(sub_arr) == k:
                sub_array_with_k_sum_dict[len(sub_arr)] = sub_arr
            all_sub_arrays.append(sub_arr)
        sub_arr = []

    max_len = 0
    for l in sub_array_with_k_sum_dict.keys():
        if l > max_len:
            max_len = l

    return sub_array_with_k_sum_dict[max_len]



def longestSubarrayWithSumK(a , k: int) -> int:
    # Write your code here
    ## Brute Force Solution:
    """
    Approach to find all subarray:
    lets say I have [1,3,4,5]
    sub array will be
    1
    1,3
    1,3,4
    1,3,4,5
    3
    3,4
    3,4,5
    4
    4,5
    5

    """
    Brute_Force_Flag = False
    if Brute_Force_Flag:
        longest_sub_arr_len = 0
        longest_sub_arr = []
        
        for i in range(len(a)):
            sub_arr = []
            for j in range(i,len(a)):
                sub_arr.append(a[j])
                if sum(sub_arr) == k:
                    if len(sub_arr) > longest_sub_arr_len:
                        longest_sub_arr_len = len(sub_arr)
                        longest_sub_arr = sub_arr

        return longest_sub_arr_len

    ## Better Solution:
    """
    [1,2,3,1,1,1,1,4,2,3]
     0,1,2,3,4,5,6,7,8,9 ----> indexes
    k = 3
    create a hashmap index wise sum up the numbers it should be less then k
    create two variables 
    pref_sum = 0, len = 0
    {sum, index}
    {1:0, pref_sum = 1, len = 0
    3:1,  pref_sum = 3, len = index+1 = 2
    6:2,  pref_sum = 6, len = 2
    7:3,  pref_sum = 7, len = 2
    8:4,  pref_sum = 8, len = 2
    9:5,  pref_sum = 9, len = 2 -----> 9 -6 =3 (k),5 -2 = 3
    }

    """
    arr_sum = 0
    longest_arr_len = 0
    longest_arr = []
    my_hashmap = {}

    for i in range(len(a)):
        arr_sum += a[i]
        if arr_sum ==k:
            longest_arr_len = max(longest_arr_len,i+1)
        
        remain = arr_sum - k
        if remain in my_hashmap.keys():
            new_len = i - my_hashmap[remain]
            longest_arr_len = max(longest_arr_len,new_len)
        
        if arr_sum not in my_hashmap.keys():
            my_hashmap[arr_sum] = i

    return longest_arr_len



if __name__ == "__main__":
    arr = [1,2,3,1,1,2,1,5,1,2,-1,1,-2,2,1,0,0,0,1,1,3,1,1,1,10,1,1,1]
    # all_sub_arrays = find_subarray(arr)
    # print(all_sub_arrays)
    # longest_arr =longest_sub_array_with_k_sum(arr,11)
    # print(longest_arr)
    longest_arr_len = longestSubarrayWithSumK(arr,11)
    print(longest_arr_len)
    print(longest_arr_len)
    
