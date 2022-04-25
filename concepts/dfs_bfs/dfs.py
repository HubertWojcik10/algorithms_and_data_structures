class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(tree, stack):
    '''NOT implementing a recursive version due to 
    the maximum recursion depth limit in Python'''
    stack.append(tree)
    while len(stack) > 0:
        node = stack.pop()
        if node is not None:
            print(node.value)
            stack.append(node.right)
            stack.append(node.left)

tree = Node('A', (Node('B', Node('D'), Node('E'))), Node('C', Node('F'), Node('G')))
dfs(tree, [])