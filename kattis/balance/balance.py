
'''
This is my solution to the Kattis Balance problem (week 2). 
The problem is to find whether a given string of parentheses is balanced.

In week 2, we learned about stacks and queues, which I used to solve this problem.
'''

stack = []
input_str = input() #e.g. (()())
open_list = ['[','(']
close_list = [']',')']
finished = False
for i in input_str:
    if not finished:
        #for every item in the string, checking what type of bracket it is, and then applying the appropriate instructions
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            pos = close_list.index(i)
            if len(stack) > 0 and open_list[pos] == stack[len(stack)-1]:
                stack.pop()
            else:
                print(0)
                finished = True

if not finished:
    if len(stack) == 0:
        #the length of the stack is 0, thus the string is balanced
        print(1)
    else:
        print(0)