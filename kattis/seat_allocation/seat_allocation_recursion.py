#This is a recursive (and non pq) solution for the Seat Allocation algorithm
# REMEMBER: this solution will not work for large numbers due to exceeding maximum recursion depth error

'''
This is a recursive (and non pq) solution for the Kattis Seat Allocation problem.
REMEMBER: this solution will not work for large numbers due to exceeding maximum recursion depth error.

GO TO seat_allocation_pq.py for the main solution and more information about the problem.
'''

def calculate(m, votes, mandates):
    print(mandates)
    if m == 0: 
        return mandates

    max = 0
    i_max = 0
    for i in range(len(votes)):
        result = votes[i] / (mandates[i] + 1)
        if result > max: 
            max = result
            i_max = i

    mandates[i_max] += 1

    print(' ')
    return calculate(m-1, votes, mandates)

#reding data from input
n, m = input().split(' ')
n, m = int(n), int(m)

#prepare the data before the calculate() function
votes = [0 for _ in range(n)]
for i in range(n):
    votes[i] = int(input())
mandates = [0 for _ in range(n)]

final_mandates = calculate(m, votes, mandates)
for mandate in final_mandates:
    print(mandate)