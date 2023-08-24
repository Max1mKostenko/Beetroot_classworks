import threading
import random
import time


"""
2. Вимірювання часу виконання:
Напишіть програму, яка виконує якусь обчислювально "важку" функцію у потоках. 
Виміряйте час виконання обчислень з використанням потоків та без них, щоб порівняти результати.
"""
rand_list = [random.randrange(100) for i in range(10000)]


def first_thread():
    list_of_dubl = []
    start_time = time.perf_counter()
    for i in rand_list:
        if rand_list.count(i) != 1:
            list_of_dubl.append(i)
    list_of_dubl_2 = list(set(list_of_dubl))
    print(list_of_dubl_2)
    end_time = time.perf_counter()
    print(f'1 It took {end_time - start_time: 0.3f} second(s) to complete.')


def second_thread():
    list_without_dublicates = []
    start_time = time.perf_counter()
    for i in rand_list:
        if rand_list.count(i) == 1:
            list_without_dublicates.append(i)
    print(list_without_dublicates)
    end_time = time.perf_counter()
    print(f'2 It took {end_time - start_time: 0.3f} second(s) to complete.')


t1 = threading.Thread(target=first_thread())
t2 = threading.Thread(target=second_thread())

# t1.run()
# t2.run()


t1.start()
t2.start()
t1.join()
t2.join()

print("\nJust func:\n")
first_thread()
second_thread()
