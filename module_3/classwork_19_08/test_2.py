import threading
from time import sleep, perf_counter
import random
"""
1. Паралельна обробка списку:
Створіть програму, яка створює два потоки. 
Перший потік обробляє парні елементи списку, а другий - непарні. 
Згодом, з'єднайте результати обробки.
"""

# from threading import Thread
# t = Thread(target=print, args=[1])
# t.run()
# >> 1


list_ = [1, 1, 2, 2, 3, 3, 4, 5, 6]
list1 = [random.randrange(100) for i in range(100)]


def first_thread():
    list_of_dubl = []
    for i in list1:
        if list1.count(i) != 1:
            list_of_dubl.append(i)
    list_of_dubl_2 = list(set(list_of_dubl))
    print(list_of_dubl_2)


def second_thread():
    list_without_dublicates = []
    for i in list1:
        if list1.count(i) == 1:
            list_without_dublicates.append(i)
    print(list_without_dublicates)


start_time = perf_counter()


t1 = threading.Thread(target=first_thread())
t2 = threading.Thread(target=second_thread())

# t1.run()
# t2.run()


t1.start()
t2.start()
t1.join()
t2.join()
end_time = perf_counter()

print(f'It took {end_time- start_time: 0.3f} second(s) to complete.')

# first_thread()
# second_thread()
# w1 = threading.Thread(name="Hello")
# w2 = threading.Thread(name="World")
#
# w1.start()
# w2.start()


