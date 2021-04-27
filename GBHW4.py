# 1
from sys import argv

file_name, worked_hour, rate, benefit = argv,

calculation = (int(worked_hour) * int(rate)) + int(benefit)
print(f"Your pay is equal {calculation}")


# 2
my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)

''' Вариант с циклом
i = 0
new= []
for el in my_list:
    if el > my_list[i-1]:
        new.append(el)
    i+=1
print(new)
'''

# 3
numbers = range(20, 241)
new_list = [el for el in numbers if el%20==0 or el%21==0]
print(new_list)


# 4
from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [1, 2, 2, 3, 4, 1, 2]
new = [el for el in my_list if my_list.count(el)==1]
print(new)


# 5
from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))

# 6
from itertools import count
from itertools import cycle

def my_count_func(start_number, stop_number):
    for el in count(start_number):
        if el > stop_number:
            break
        else:
            print(el)
def my_cycle_func(my_list, iteration):
    i = 0
    iter = cycle(my_list)
    while i < iteration:
        print(next(iter))
        i+=1
my_count_func(start_number = int(input("enter start number: ")), stop_number = int(input("enter stop number: ")))
my_cycle_func(my_list = [1, 2], iteration = int(input("enter iteration: "))) 

# 7
def fibo_gen(number):
    count = 1
    while count <= number:
        yield count
        count += 1
i = 1
my_fifteen = []
for el in fibo_gen(5):
    if i > 15:
        break
    else:
        my_fifteen.append(el)
        i += 1
print(my_fifteen)