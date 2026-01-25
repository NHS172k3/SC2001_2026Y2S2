# def maxmin(A:list) -> list:
#     if len(A) > 1:
#         mid = len(A) // 2
#         leftmaxmin = maxmin(A[:mid])
#         rightmaxmin = maxmin(A[mid: ])
#     else:
#         return (A[0],A[0])
    
#     return merge(leftmaxmin, rightmaxmin)



# def merge(left:tuple, right:tuple)->tuple:
#     return (max(left[0], right[0]), min(left[1], right[1]))



# At the very bottom of the call stack, u have n/2 * 2 = n comparisons for max and min each.
# Above that, we have n/4 * 2 comparisons which is n/2
# Above that, its n/8 * 2 = n/4 comparisons
#.... Eventually, its (2 + 4 + 8 + ... + n/2 + n) = 2+4+8+...+ 2^(k-1) + 2^(k) = 2^(k+1) - 2 = 2n - 2 = 2(n)



def maxmin(A:list) -> list:
    
    def comparisons(A):
        minlist, maxlist = [], []

        index = 0
        while index <= len(A) - 2:
            if A[index] <= A[index+1]:
                minlist.append(A[index])
                maxlist.append(A[index+1])
            else:
                minlist.append(A[index+1])
                maxlist.append(A[index])
            index += 2
        if len(A) % 2 == 1:
            if A[len(A) - 1] <= A[0]:
                minlist.append(A[len(A) - 1])
            else:
                maxlist.append(A[len(A) - 1])
        
        return maxlist, minlist

    maxlist, minlist = comparisons(A)

    while len(maxlist) > 1:
        maxlist, _ = comparisons(maxlist)  

    
    while len(minlist) > 1:
        _, minlist = comparisons(minlist)

    return (maxlist[0], minlist[0])

if __name__ == "__main__":
    print(maxmin([14, -1, 7, 0, 4, -9]))

# Now, we do pairwise comparison of the elements from the start of the list
# Hence, n/2 comparisons in first round. Only this, because they asked us to assume n = 2^k which means even elements
# Then, we derive two lists of n/2 length each amongst which we will do n/4 comparisons each so total n/2 comparisons
# Next we have 2 lists of n/4 length each, so a total of n/4 comparisons.
# ... all the way until we have 2 lists of 2, so a total of 2 comparisons
# 2 + 4 + 8 +... + 2^(k-1) + 2^(k-1) = 2^(k) - 2 + 2^(k-1) = 1.5n - 2




