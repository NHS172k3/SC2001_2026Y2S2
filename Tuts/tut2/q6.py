def duplicate_check(A):
    return len(A) > len(set(A))

print(duplicate_check([1,3,2,4]))

# In the worst case if we have collisions between the elements that are being hashed due to poor hash function,
# we get an issue where the worst time complexity is of order O(n^2) since we have to do the collision avoidance of O(n) for n elements.

def partc(A):
    # Since we know the elements are integers from this list of 1 to 2n, we can basically create an array called seen
    seen = [False] * 2* len(A)
    for i in A:
        if seen[i]:
            return True
        seen[i] = True
    return False
print(partc([1,3,2,7]))