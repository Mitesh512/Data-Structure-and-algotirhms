# Quick Sort Algorithm:

"""
What do we do in Quick sort algorithm:

Pick a Pivot point.

we put the pivot point at its right postion.
for example:
[4, 2, 7, 8, 1, 3]

we pickup pivot 4 and will try to put at its correct place.

smaller on left of pivot and larger on right of pivot
search 1 to n
is 2 < 4 (pivot)?
    yes [shift to left index]
    2,4,7,8,1,3
    is 7 < 4 ?
    No
    is 8 < 4 ?
    No
    is  1 <4?
    Yes
    shift 1 to left index of 4 and similarily increase the indexes of 4,7,8
    2,1,4,7,8,3
    is 3 < 4?
    yes
    2,1,3,4,7,8

    
after step 1 , we can say for sure that 4 is at correct position.
left smaller is yet to be sorted right greated is also yet to be sorted.

lets take 2,1,3
pickup a pivot that is 2

is 1< 2?
yes
    1,2,3
    is 3<2?
    no
    1,2,3
left is sorted

go to right
7,8
select pivot as 7,
is 8 < 7?
No
7,8

add left sorted  + pivot + right array

1,2,3,4,7,8
#### How to write the logic
[4,2,7,8,1,3]
 0,1,2,3,4,5
 i         j 
low        high

select pivot (4)
lets find the first element grater then my pivot

iterate through i 0 to n
is 4 greater then pivot? No
is 2 greater then pivot? No
is 7 greater then pivot? Yes ----> identified (low i position is 2 now)
    now check from high to low find the first element lower then pivot
    is 3 less then 4? Yes ------> identified (high j position is 5 now)
    swap them
    4,2,3,8,1,7

    # again start from left where you left off (i from 3 )
    is 8 greater then 4? yes ---> identified (low is 3 now)
    now check from j (4)
    is 1 less than 4 yes? ----> identified (high j is 4 now)
    swamp them

    4,2,3,1,8,7
    again check from low
    is 1 greater then 4 No?
    check condition is i 3(low) greater than high j 4? No 
    is 8 grater then 4 yes? lets check if 4(low i) has crossed  j(4) no
    is 8 less then 4 no
    is 1 less than 4 yes (is high 3 less than low 4) Yes we stop here

    Swap 3 (j) with first

    1,2,3,4,8,7

1,2,3,4,8,7

Now 4 has been placed at right postion, left side of pivot 4 are smaller than 4 and right are greater then 4
Now index i (3) can be called as partition index

Arrays to be sorted
low_array low to partition-1 [1,2,3]
high_array partition+1 to high [7,8]
apply same again

------------------------------------------------------------------------
Pseudo Code:

def find_pivot_position(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while (arr[i] <= arr[pivot]) and (i<=high):
            i += 1
        while (arr[j] > arr[pivot]) and (j>= low):
            j -= 1
        
        if (i<j):
            arr[i],arr[j] = arr[j],arr[i]
    arr[pivot],arr[j] = arr[j],arr[pivot]

    return j
            
        


def quick_sort(arr,low,high):
    if low < high:
        partition_index = find_pivot_position(arr,low,high)

        quick_sort(arr,low,partition_index )
        quick_sort(arr,partition_index+1,high +1)

"""

def find_pivot_position(arr,low,high,is_asc = False):
    pivot = arr[low]
    i = low
    j = high

    if is_asc:
        while i < j:
            while (arr[i] <= pivot) and (i <= high-1):
                i += 1
            while (arr[j] > pivot ) and (j >= low+1):
                j = j-1
            if (i<j):
                arr[i],arr[j] = arr[j],arr[i]
    else:
        while i < j:
            while (arr[i] >= pivot) and (i <= high):
            
                i += 1
            while (arr[j] < pivot ) and (j >= low):
                j = j-1
            if (i<j):
                arr[i],arr[j] = arr[j],arr[i]

    arr[low],arr[j] = arr[j],arr[low]

    return j

def quick_sort(arr,low,high):
    if low < high:
        partition_index = find_pivot_position(arr,low,high,is_asc=True)
        print("Partition Index is", partition_index , arr)
        quick_sort(arr,low,partition_index-1)
        quick_sort(arr,partition_index+1,high)
    return arr


if __name__ == "__main__":
    arr = [4, 2, 7, 8, 1, 3]
    low = 0
    high = len(arr) -1 
    print(arr,low,high)

    arr = quick_sort(arr,low,high)

    print(arr)
