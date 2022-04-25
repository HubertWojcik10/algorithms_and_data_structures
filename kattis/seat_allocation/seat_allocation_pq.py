from itu.algs4.sorting.max_pq import MaxPQ
'''
This is my solution to the Kattis Seat Allocation problem (week 5). 
The problem is to allocate seats for each party in a parliament.

In week 5, we learned about Priority Queues, and I used the MaxPQ to solve this problem.
'''

def calculate(m, pq, votes, mandates):
    #calculating the number of mandates for each party using PriorityQueue algorithm
    for _ in range(m):
        max_node = votes.index(pq.del_max())
        mandates[max_node] += 1

        votes[max_node] = first[max_node] / (mandates[max_node] + 1)
        pq.insert(votes[max_node])

    return mandates


#reading data from input
n, m = input().split(' ')
n, m = int(n), int(m)

#preparing data for the calculate function
votes = [0 for _ in range(n)]
pq = MaxPQ()
mandates = [0 for _ in range(n)]
for i in range(n):
    votes[i] = (int(input()))
    pq.insert(int(votes[i]))
first = votes.copy()


final_mandates = calculate(m, pq, votes, mandates)
for mandate in final_mandates:
    print(mandate)