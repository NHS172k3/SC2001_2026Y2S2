'''
a) Write code to count the numbers of valid linearizations by enumerating
all possible ways (all permutations) to sort the nodes, then check if the sort
results in a valid linearization.
'''



import math
adj_list = {"C":["D","H"], "D":["B"], "H":["B", "G"], "B":["A", "E"], "G":["A"],"E":["F"], "A":[], "F":[]}
# Now we need to check make all permutations of "ABCDEFGH" and check in the linearization, theres no backward arrow
# This is equivalent to checking if there is no forward arrow in the reverse of the permutation
node_list = list(adj_list.keys())
print(node_list)
# We can do backtracking for this
res = []
sol = []

def dfs(node_list, visited):
    if len(visited) == len(node_list):
        res.append(sol[:])
    for i in node_list:
        if i not in visited:
            sol.append(i)
            visited.add(i)
            dfs(node_list, visited)
            visited.remove(i)
            sol.pop()
visited = set()
dfs(node_list, visited)
# Now res has all the permutations
# Count valid combinations by checking if any of them have an unvisited value in their adj list.(remember that for any list, its reverse also inside)


num = 0
for perm in res:
    earlier = set()
    valid = True
    for i in perm:
        earlier.add(i)
        for node in adj_list[i]:
            if node in earlier:
                valid = False
                break
        if not valid:
            break
    if valid:
        num += 1
print(num)
        


    



