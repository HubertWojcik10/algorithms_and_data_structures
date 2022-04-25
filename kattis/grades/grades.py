
'''
This is my solution to the Kattis Grades problem (week 4). 
The problem is to sort a list of students by their grades.

In week 11, we learned about sorting algorithms, which I used to solve this problem.
'''

def sort(arr):
    grades = 'A, B, C, D, E, FX, F'.split(', ')
    N = len(arr)
    for i in range(1, N):
        for j in range(i, 0, -1):
            letter_grade, additional, plus = _split_grade(arr[j][1])
            letter_grade_prev, additional_prev, plus_prev = _split_grade(arr[j-1][1])

            name, name_prev = arr[j][0], arr[j-1][0]

            #the better the grade, the lower the index
            if grades.index(letter_grade) > grades.index(letter_grade_prev): 
                break
            
            #checking the minuses and pluses
            elif grades.index(letter_grade) == grades.index(letter_grade_prev):
                if plus == False and plus_prev == True:
                    break
                elif plus == False and plus_prev == False:
                    if len(additional) > len(additional_prev): 
                        break
                elif plus == True and plus_prev == True:
                    if len(additional) < len(additional_prev): 
                        break

            #if grades are exactly the same, sort alphabetically
            if arr[j][1] == arr[j-1][1]:
                tmp = sorted([name_prev, name])
                if name_prev == tmp[0]:
                    break


            _exchange(arr, j, j - 1)
    return arr
            

def _exchange(a, i: int, j: int):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def _split_grade(grade):
    '''
    splits the grade into a letter (A, B, C, ...) and the add-ons (++, -, ...)
    '''
    letter_grade, additional = '', ''
    plus = False
    no_char = True
    for i in grade:
        if i == '-' or i == '+':
            letter_grade = grade[:grade.index(i)]
            additional = grade[grade.index(i):]
            no_char = False

        if i == '-': plus=False
        else: plus = True

    if no_char: return grade, '', False

    return letter_grade, additional, plus



#preparing the input for the main sort() function
n = int(input())
info_arr = []
for i in range(n):
    name, grade = input().split(' ')
    info_arr.append((name, grade))

final_arr = sort(info_arr)


#printing only the names (required by Kattis)
for i in final_arr:
    print(i[0])