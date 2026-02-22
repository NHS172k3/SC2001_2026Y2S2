def maxmin(A:list) -> list:
    if len(A) == 1:
        return (A[0], A[0])
    elif len(A) == 2:
        return (A[0], A[1]) if A[0] >= A[1] else (A[1], A[0])
    else:
        mid = len(A)//2
        maxleft, minleft = maxmin(A[:mid])
        maxright, minright = maxmin(A[mid:])
        max_val = max(maxleft, maxright)
        min_val = min(minleft, minright)
        return (max_val, min_val)
        
if __name__ == "__main__":
    print(maxmin([14, -1, -17, 0, 4, -9]))
    #print(maxmin([14, 15]))





