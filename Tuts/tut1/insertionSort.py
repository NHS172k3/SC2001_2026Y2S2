def insertionSort(A: list) -> list:
    
    comparisons = 0
    for index in range(1, len(A)):
        # Here we store the to-be-replaced value in a key and shift the elements until our intended element is reached
        j, key = index, A[index]

        while j > 0 and key <= A[j-1]:
            comparisons += 1
            A[j] = A[j-1]
            j -= 1
        
        A[j] = key

    
    return A, comparisons




if __name__ == "__main__":
    listTest = []
    for i in range(0, 100000):
        listTest.append(i)
    listTest.extend([0, -2, -4, -6, -8])
    print(insertionSort(listTest))