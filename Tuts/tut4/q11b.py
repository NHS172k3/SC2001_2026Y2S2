'''
Formulate the counting problem as a graph traversal (hint: look up lecture
nodes on 8-queens formulation). Define the new graph structure (hint: it is a
tree called a “search tree”). What are the nodes? What are the edges? What is the
root node? Then use graph traversal to count the number of valid linearizations.
'''

# Backtracking to find valid combos
adj_list = {"C":["D","H"], "D":["B"], "H":["B", "G"], "B":["A", "E"], "G":["A"],"E":["F"], "A":[], "F":[]}
permutations = set()

node_list = list(adj_list.keys())
valid = 0

def dfs():
    global valid
    # print(permutations)  # Debug: uncomment to see all states
    if len(permutations) == len(node_list):
        valid += 1
        return
    for i in node_list:
        if i not in permutations:
            validity = True
            for ele in adj_list[i]:
                if ele in permutations:
                    validity = False
                    break
            if validity:
                permutations.add(i)
                dfs()
                permutations.remove(i)

dfs()
print(valid)
        




# We can also attempt to find the in-degree of each node and if lets say the node's parent alr came, we minus 1 for the indegree of that node
# We only add nodes with 0 indegree as a result.
indegree_dict = {x:0 for x in node_list}
for i in list(adj_list.values()):
    for j in i:
        # constructing the indegree dictionary
        indegree_dict[j] += 1

valid = 0
permutations = set()
def dfs_optimized():
    global valid
    if len(permutations) == len(node_list):
        valid += 1
        return
    for i in node_list:
        if i not in permutations and indegree_dict[i] == 0:
            permutations.add(i)
            for child in adj_list[i]:
                indegree_dict[child] -= 1
            dfs_optimized()
            for child in adj_list[i]:
                indegree_dict[child] += 1
            permutations.remove(i)

dfs_optimized()
print(valid)


# By using indegree, we now have an optimized version where we 
# store information about who has alr occured to make an informed decision
    



