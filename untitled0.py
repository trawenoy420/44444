# --------- ПУНКТ 1 ----------

from sys import argv

if len(argv) > 1:
    name_script, time_work, rate, prize = argv
    time_work = int(time_work)
    rate = int(rate)
    prize = int(prize)
    print((time_work * rate) + prize)
else:
    time_work = int(input("Inpute time work: "))
    rate = int(input("Inpute ratet: "))
    prize = int(input("Inpute prize: "))
    print((time_work * rate) + prize)

# --------- ПУНКТ 2 ----------

my_list = [3, 20, 9, 5, 1, 8, 11, 6, 15]
new = [el for el in my_list if el > my_list[my_list.index(el)-1]]
print(new)

# --------- ПУНКТ 3 ----------

numbers = range(20, 241)
new_list = [el for el in numbers if el%20==0 or el%21==0]
print(new_list) 

# --------- ПУНКТ 4 ----------

from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [1, 2, 2, 3, 4, 1, 2, 3, 12, 55, 55, 103, 36]
new = [el for el in my_list if my_list.count(el)==1]
print(new) 

# --------- ПУНКТ 5 ----------

from functools import reduce
my_list = [el for el in range(100, 1001) if el % 2 == 0]
def my_func(prev_el, el):
    return prev_el * el

print(reduce(my_func, my_list))

# --------- ПУНКТ 6 ----------

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


