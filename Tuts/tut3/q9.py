'''
Q9 Given k lists with a total of n numbers, where k ≥ 2 and each list has
been sorted in decreasing order, design an algorithm to merge the k lists into
one list sorted in decreasing order, with running time O(n log2 k).
'''


class MaxHeap:
    """A max-heap implementation for merging k sorted lists."""

    def __init__(self):
        self.heap = []
    
    def heapify(self, arr):
        self.heap = arr[:]  # Copy the array
        # Start from last non-leaf node
        for i in range(len(self.heap)//2 - 1, -1, -1):
            self.fixheap(i, 2*i + 1)
        

        
    def fixheap(self, curr, compare):
        # Heap's topmost element needs to be fixed in
        while compare < len(self.heap):
            # Find the larger child (compare by value, which is index 1 in tuple)
            if compare + 1 < len(self.heap) and self.heap[compare + 1][1] > self.heap[compare][1]:
                compare += 1
            # If current is larger than both children, done (compare by value)
            if self.heap[curr][1] >= self.heap[compare][1]:
                break
            # Swap and continue down
            self.heap[curr], self.heap[compare] = self.heap[compare], self.heap[curr]
            curr = compare
            compare = 2 * curr + 1


    def checkMax(self):
        if not self.heap:
            return None
        max_val = self.heap[0]
        return max_val




def merge_k_sorted_lists(lists):
    """
    Merge k sorted lists (in decreasing order) into one sorted list (decreasing order).
    Time complexity: O(n log k) where n is total number of elements
    
    Args:
        lists: List of k sorted lists, each sorted in decreasing order
    
    Returns:
        A single list with all elements sorted in decreasing order
    """
    # Create heap instance
    heap = MaxHeap()
    
    # Put first element from each list into heap, including its list index as a tuple
    initial = []
    for index, lst in enumerate(lists):
        if lst:
            initial.append((index,lst[0]))
    
    # Heapify the initial elements
    heap.heapify(initial)
    
    result = []
    list_indices = [1] * len(lists)
    
    while heap.heap:
        # Extract max (tuple: (list_index, value))
        max_tuple = heap.checkMax()
        list_idx, max_val = max_tuple
        result.append(max_val)  # Append just the value
        
        # If the list_idx is already at the end of the list
        if list_indices[list_idx] >= len(lists[list_idx]):
            list_idx = 0
            while list_idx < len(lists) and list_indices[list_idx] >= len(lists[list_idx]):
                list_idx += 1
        
        toAdd = list_idx < len(lists) # Whether need to add from new list or not

        if toAdd:
            next_val = lists[list_idx][list_indices[list_idx]]
            heap.heap[0] = (list_idx, next_val)  # Replace at position 0
            list_indices[list_idx] += 1 
        else:
            last_tuple = heap.heap.pop()
            if heap.heap:  # Only replace if heap is not empty
                heap.heap[0] = last_tuple

        # Fix heap after insertion
        if heap.heap:  # Only fix if heap is not empty
            heap.fixheap(0, 1)
        
    return result


def main():
    # Test cases
    test_cases = [
        # Test case 1: Basic example
        [[9, 7, 5, 3], [8, 6, 4, 2], [10, 1]],
        
        # Test case 2: Single list
        [[5, 4, 3, 2, 1]],
        
        # Test case 3: Multiple lists with varying lengths
        [[20, 15, 10], [18, 12, 8, 5], [19, 14], [17, 11, 6, 3, 1]],
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test case {i}:")
        print(f"Input: {test}")
        result = merge_k_sorted_lists(test)
        print(f"Output: {result}")
        print()


if __name__ == "__main__":
    main()