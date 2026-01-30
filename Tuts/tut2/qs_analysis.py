import quicksort 
import matplotlib.pyplot as plt
from itertools import permutations

def main(num):
    base_lst = [x for x in range(num+1)]
    comparison_list = []

    for perm in permutations(base_lst):
        lst = list(perm)  # Convert tuple to list
        _, comparisons = quicksort.quicksort(0, num, lst, 0)
        comparison_list.append(comparisons)
    
    return comparison_list

        

plt.hist(main(20), bins = 20)
plt.show()