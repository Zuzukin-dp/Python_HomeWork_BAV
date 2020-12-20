# параметры функций
# *args, **kwargs
# работа с файлами
# time, sys, os, os.path

import random
import string

with open("Homeworks/lesson7.txt", "r") as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.strip())

print(len(data), type(data))
for line in data:
    print(line)

data.append("Всем хорошего вечера!")

with open("Homeworks/lesson7.txt", "w") as txt_file:
    txt_file.write("\n".join(data))







# print(string.ascii_lowercase)
DEBUG_MODE = True

def create_random_str(str_len, debug_mod=DEBUG_MODE):
    alphabet = list(string.ascii_lowercase)
    random.shuffle(alphabet)
    random_str = "".join(alphabet[:str_len])
    if debug_mod:
        print(random_str)
    return random_str


def testing_args(q, w, e, r, t, y, debug_mod=DEBUG_MODE):
    if debug_mod:
        print(q, w, e, r, t, y)

random_str = create_random_str(10)
testing_args(1,2,3,4,5,6, )




def testing_default_values(first, second=100):
    result = str(first) + str(second)
    return result

result = testing_default_values("12")
print(result)

testing_args("q", "w", r=1, y=2, t=0, e="e")








def crate_random_point(min_value, max_value):
    point = (random.randint(min_value, max_value),
             random.randint(min_value, max_value),
             random.randint(min_value, max_value))
    return point


def create_line_segment(start, stop):
    line_segment = {"A": crate_random_point(start, stop),
                    "B": crate_random_point(start, stop)}
    return line_segment


min_value, max_value = -100, 100
point_max = crate_random_point(min_value, max_value)
print(point_max)

min_limit, max_limit = -10, 10
point = crate_random_point(min_limit, max_limit)
print(point)
stop = 100
start = 10
AB = create_line_segment(10, 100)  # Позиционные аргументы
AB = create_line_segment(start, stop=stop)  # Именованные аргументы
print(AB)
