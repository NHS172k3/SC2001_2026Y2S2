'''
Q5 Each of n elements in an array may have one of the key values red, white, or blue. 
Give an efficient algorithm for rearranging the elements so that all the reds come before all the whites, and all the whites come before all the blues. 
(It may happen that there are no elements of one or two of the colours.) 
The only operations permitted on the elements are examination of a key to find out what colour it is, and a swap, or interchange, of two elements (specified by their indices). 
What is the asymptotic order of the worst case running time of your algorithm? (There is a linear-time solution.)
'''

# Partition the elements in a way that u first find a white and a blue and then make them less than for each one

colour_priority = {"blue": 2, "white": 1, "red": 0}
def partition(pivot, target, colours):
    colours = swap(pivot, 0, colours)
    last_small = 0
    element = 1
    while element <= len(colours) - 1:
        if colour_priority[colours[element]] < colour_priority[target]:
            colours = swap(element, last_small+1, colours)
            last_small += 1
        # We can do this because everything between element and last_small has ideally already been searched and settled. so we can always increment
        element += 1

    
    # Now we need to putback the element into the position of last_small + 1
    colours = swap(0, last_small, colours)
    return colours

def swap(first, second, array):
    array[first], array[second] = array[second], array[first]
    return array
def coloursort(colours):
    for element in range(len(colours)):
        if colours[element] == "blue":
            colours = partition(element, "blue", colours)
            break
    print(colours)
    for element in range(len(colours)):
        if colours[element] == "white":
            colours = partition(element, "white", colours)
            break
    return colours

print(coloursort(["red", "blue", "blue", "red", "white", "blue", "white", "white", "blue", "red", "white"]))
        
