def merge(A: list, B: list) -> tuple:  # Return merged list and comparison count
    res = []
    Ap, Bp = 0, 0
    comparisons = 0
    while Ap < len(A) or Bp < len(B):
        if Ap >= len(A):
            res.append(B[Bp])
            Bp += 1
        elif Bp >= len(B):
            res.append(A[Ap])
            Ap += 1
        elif A[Ap] >= B[Bp]:
            comparisons += 1
            res.append(B[Bp])
            Bp += 1
        else:
            comparisons += 1
            res.append(A[Ap])
            Ap += 1
    return res, comparisons


def mergeSort(A: list) -> tuple: 
    
    if len(A) <= 1:
        return A, 0
    mid = len(A) // 2
    leftArr, left_comps = mergeSort(A[:mid])
    rightArr, right_comps = mergeSort(A[mid:])
    merged, merge_comps = merge(leftArr, rightArr)
    total_comps = left_comps + right_comps + merge_comps
    return merged, total_comps


if __name__ == "__main__":
    sorted_list, comps = mergeSort([23]*8)
    print(sorted_list, comps)