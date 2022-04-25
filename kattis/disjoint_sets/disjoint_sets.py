from itu.algs4.fundamentals.uf import UF
from itu.algs4.stdlib.stdio import readInt, writeln

'''
This is my solution to the Kattis Disjoint Sets problem (week 1). 
The problem is to maintain a family of disjoint sets and apply the operations of query, union, and find.

In week 1, we learned about union-find, which I used to solve this problem.
'''

#for finding a solution to the problem, I used algs4 library provided by ITU
n = readInt()
m = readInt()
uf = UF(n) #union find class

def move(uf, s, t):
    uf._parent[s] = uf._parent[t]

for i in range(0, m):
    type = readInt()
    s = readInt()
    t = readInt()

    if type == 0:
        if uf.connected(s, t): writeln(1)
        else: writeln(0)
    elif type == 1:
        uf.union(s, t)
    elif type == 2:
        move(uf, s, t)

