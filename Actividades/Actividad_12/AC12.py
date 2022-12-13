from random import uniform
from collections import deque

queue_1 = deque()
queue_2 = deque()

arr_range(1, 3)
exit_range = (1, 10)

current_time = 0


class Person:
    pass

arr_time_1 = uniform(arr_range)
arr_time_2 = uniform(arr_range)
exit_time_1 = uniform(exit_range)
exit_time_2 = uniform(exit_range)

while True:

    current_time = min(arr_time_1, arr_time_2, exit_time_1, exit_time_2)

    if current_time == arr_time_1:
    	queue_1.append(Person)
    if current_time == arr_time_2:
    	queue_2.append(Person)
    if current_time == exit_time_1:
    	queue_1.popleft(Person)
    if current_time == exit_time_2:
    	queue_1.popleft(Person)

    arr_time_1 -= current_time
    arr_time_2 -= current_time
    exit_time_1 -= current_time
    exit_time_2 -= current_time

    for time in [arr_time_1, arr_time_2]:
    	if time == 0:
    		time = uniform(arr_range)
    for time in [exit_time_1, exit_time_2]:
    	if time == 0:
    		time = uniform(exit_range)



