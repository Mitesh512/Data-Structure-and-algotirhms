# Recursion: Funcitons calls self, till a specified condition is met

# important points in recursion
# backtracking --> n - i - 1

def back_track_rec_n_to_1(i,n):
    if i == n + 1:
        return
    else:
        back_track_rec_n_to_1(i+1,n)
        print(i)


def check_palindrome(str,i):
    if i >= len(str)/2:
        return True
    if str[i] != str[len(str)-i-1]:
        return False
    else:
        return check_palindrome(str,i+1)

def get_fibonacci_number(n):
    if n <=1:
        return n
    else:
        return get_fibonacci_number(n-1) + get_fibonacci_number(n-2)

# time complexity 2^n



def get_subsequences(ind,seq,arr,n):
    """ 
    # Printing all the subsequences using Recursion
    # pring all sub sequences:
    # Example: [3,1,2]

    3
    1
    2
    31
    12
    32 [Non - contigous] but is subsequence [follows the True Order]
    31
    2"""

    if ind > n:
        if len(seq)>0:
            print(seq)
        return
    seq.append(arr[ind])
    get_subsequences(ind+1, seq, arr,n)
    seq.pop()
    get_subsequences(ind+1, seq, arr, n)


    """
 
    How it works is:
    for above example you have an array of 3 values and you have to get all the subsequeces:
    consider indexes below 0 as No, and 1 as yes
    
    _ _ _
    
    1 0 0 ---> 3
    1 1 0 ---> 3,1
    0 1 0 ---> 1
    and so on its matter of chosing and not chosing

    Base condition would be the last index n
    f(ind,seq):
        if ind >= n:
            print(seq)
            return
        seq.append[arr[ind]]
        f(ind+1,seq)  #----> chosing the next index
        seq.pop()
        f(ind+1,seq)

    Lets try to understand few steps:

    def get_subsequences(0,[],[3,1,2],2):

    if 0 > 2: ---> False
        if len(seq)>0:
            print(seq)
        return
    [].append(arr[0]) ----> [3]
    --->get_subsequences(ind+1, seq, arr,n)
        get_subsequences(1,[3],[3,1,2],2):
        if 1 > 2: --> False
            if len(seq)>0:
                print(seq)
            return
        [3].append(arr[1]) ---> [3,1]
        --->get_subsequences(ind+1, seq, arr,n)
            get_subsequences(2,[3,1],[3,1,2],2):
            if 2 > 2: ---> False
                if len(seq)>0:
                    print(seq)
                return
            [3,1].append(arr[2]) ----> [3,1,2]
            --->get_subsequences(ind+1, seq, arr,n)
                get_subsequences(3,[3,1,2],[3,1,2],2):
                if 3 > 2: ---> True
                    if len([3,1,2])>0: ---> True 
                        print([3,1,2])-----------------------> [3,1,2]
                    return
            [3,1,2].pop() ----> [3,1]
            --->get_subsequences(ind+1, seq, arr, n)
                get_subsequences(3,[3,1],[3,1,2],2):
                if 3 > 2: --> True
                    if len(seq)>0: ---> True
                        print([3,1])------------------------->[3,1]
                    return
        [3,1].pop() ---> [3]
        --->get_subsequences(ind+1, seq, arr, n)
            def get_subsequences(2,[3],[3,1,2],2):
            if 2 > 2: ---> False 
                if len(seq)>0:
                    print(seq)
                return
            [3].append(arr[2]) ----> [3,2]
            --->get_subsequences(ind+1, seq, arr,n)
                def get_subsequences(3,[3,2],arr,n):
                if 3 > 2:
                    if len([3,2])>0:
                        print(seq) -------------------------> [3,2]
                    return
            [3,2].pop() ----> [3]
            --->get_subsequences(ind+1, seq, arr, n)
                get_subsequences(3,[3],arr,n):
                if 3 > 2:
                    if len([3])>0:
                        print(seq) -------------------------> [3]
                    return
    [3].pop() -----> []
    --->get_subsequences(ind+1, seq, arr, n)
        get_subsequences(1,[],[3,1,2],2):
        if 1 > 2: ---> False
            if len(seq)>0:
                print(seq)
            return
        seq.append(arr[ind])
        get_subsequences(ind+1, seq, arr,n)
        seq.pop()
        get_subsequences(ind+1, seq, arr, n)
    ------
    ----
    --
    and so on................!

    """

    return

def get_subseq(ind,seq,arr,n):
    # define the base condition
    if ind > n:
        if len(seq):
            print(seq)
        return
    
    seq.append(arr[ind])
    get_subseq(ind+1,seq,arr,n)
    seq.pop()
    get_subseq(ind+1,seq,arr,n)

    return


# return all the sequences where sum is 4
def get_subseq_for_given_sum(ind, seq,arr,n,s):
    # define the base condition
    if ind > n:
        if sum(seq) == s:
            print(seq,sum(seq))
        return
    
    seq.append(arr[ind])
    get_subseq_for_given_sum(ind+1,seq,arr,n,s)
    seq.pop()
    get_subseq_for_given_sum(ind+1,seq,arr,n,s)
    return


# get exactly the first instance where sum is achieved
def get_first_subseq_for_given_sum(ind,seq,arr,n,s):
	# define the base condtion
	if ind> n:
		if sum(seq) == s:
			return seq
		return False
	
	seq.append(arr[ind])
	if get_first_subseq_for_given_sum(ind+1,seq,arr,n,s):
		return seq
	seq.pop()
	if get_first_subseq_for_given_sum(ind+1,seq,arr,n,s):
		return seq
	return False



def get_count_subseq_for_sum(ind,seq,arr,n,s):
	# define the base condtion
	if ind> n:
		if sum(seq) == s:
			print(seq)
			return 1
		else:
			return 0
	
	seq.append(arr[ind])
	l = get_count_subseq_for_sum(ind+1,seq,arr,n,s)
	seq.pop()
	r = get_count_subseq_for_sum(ind+1,seq,arr,n,s)
	
	return l + r


if __name__ == "__main__":
    arr = [3,1,2,4,5]
    n = len(arr)  -1
    get_subsequences(0,[],arr,n)

