#####################################################
# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.

import random

my_rnd_list = [random.randint(1, 100) for _ in range(20)]
print(my_rnd_list)

my_rnd_list2 = []
for _ in range(20):
    my_rnd_list2.append(random.randint(1, 100))
print(my_rnd_list2)

#####################################################
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random
# в диапазоне от -100 до 100 по каждой оси.

import random

triangle = {"A": (random.randint(-100, 100),
                  random.randint(-100, 100),
                  random.randint(-100, 100)),
            "B": (random.randint(-100, 100),
                  random.randint(-100, 100),
                  random.randint(-100, 100)),
            "C": (random.randint(-100, 100),
                  random.randint(-100, 100),
                  random.randint(-100, 100))
            }

print(triangle)


#####################################################
# 3) Создать функцию print_stars, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = "I'm the string"
# print_stars(my_str)
# Печатает ***I'm the string***

def print_stars(var_str: str):
    var_my_str = '***' + var_str + '***'
    print(var_my_str)
    return var_my_str


# my_str = "I'm the string"
my_str = input('Input something:')
print_stars(my_str)

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена с этим возрастом.

persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 25},
           {"name": "Will", "age": 37},
           {"name": "Donald", "age": 15},
           {"name": "Greg", "age": 24}
           ]

for key_pers in persons:
    age_pers = [age_pers["age"] for age_pers in persons]
    if key_pers['age'] == min(age_pers):
        print(key_pers['name'])

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена этой длинны.

persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 25},
           {"name": "Patric", "age": 37},
           {"name": "Donald", "age": 15},
           {"name": "Greg", "age": 24}
           ]

for pers_nm in persons:
    len_pers_nm = [len(pers_nm['name']) for pers_nm in persons]
    if len(pers_nm['name']) == max(len_pers_nm):
        print(pers_nm['name'])

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# в) Посчитать среднее количество лет всех людей из списка.

persons = [{"name": "John", "age": 15},
           {"name": "Jack", "age": 25},
           {"name": "Patric", "age": 37},
           {"name": "Donald", "age": 15},
           {"name": "Greg", "age": 24}
           ]

for obj in persons:
    all_age = [age_pers['age'] for age_pers in persons]
    mean_age = sum(all_age) / len(all_age)
print(mean_age)

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 5) Даны два словаря my_dict_1 и my_dict_2.
# а) Создать список из ключей, которые есть в обоих словарях.

my_dict_1 = {"name": "Greg", "age": 29, "job": "SMM", "works": ["CSS", "PHP"]}
my_dict_2 = {"name": "Bob", "hobby": "snowboarding", "work": "CSS", "age": 34}

union_list = []
for key in my_dict_1:
    if key in my_dict_2:
        union_list.append(key)
print(union_list)

# union_list = []
# for key_md_1 in my_dict_1:
#     for key_md_2 in my_dict_2:
#         if key_md_1 == key_md_2:
#             union_list.append(key_md_1)
# print(union_list)

# t1 = []
# t2 = []
# for key_md_1 in my_dict_1:
#     t1.append(key_md_1)
#     for key_md_2 in my_dict_2:
#         t2.append(key_md_2)
#         uni_list = list(set(t1).intersection(set(t2)))
# print(uni_list)

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 5) Даны два словаря my_dict_1 и my_dict_2.
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.

my_dict_1 = {"name": "Greg", "age": 29, "job": "SMM", "works": ["CSS", "PHP"]}
my_dict_2 = {"name": "Bob", "hobby": "snowboarding", "work": "CSS", "age": 34}

union_list = []
for key in my_dict_1:
    if key not in my_dict_2:
        union_list.append(key)
print(union_list)

# t1 = []
# t2 = []
# for key_md_1 in my_dict_1:
#     t1.append(key_md_1)
#     for key_md_2 in my_dict_2:
#         t2.append(key_md_2)
#         uni_list = list(set(t1).difference(set(t2)))
# print(uni_list)

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 5) Даны два словаря my_dict_1 и my_dict_2.
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.

my_dict_1 = {"name": "Greg", "age": 29, "job": "SMM", "works": ["CSS", "PHP"]}
my_dict_2 = {"name": "Bob", "hobby": "snowboarding", "work": "CSS", "age": 34}

new_dict = {}
for key, value in my_dict_1.items():
    if key not in my_dict_2:
        new_dict[key] = value
print(new_dict)

# t1 = []
# t2 = []
# new_dict = {}
# for key_md_1 in my_dict_1:
#     t1.append(key_md_1)
#     for key_md_2 in my_dict_2:
#         t2.append(key_md_2)
#         uni_list = list(set(t1).difference(set(t2)))
# # print(uni_list)
# for key_lst in uni_list:
#     for key, value in my_dict_1.items():
#         if key_lst == key:
#             new_dict[key] = value
#             # print(key, value, key_lst)
# print(new_dict)

#####################################################
# Задания 4 и 5 выполнять с помощью циклов
# 5) Даны два словаря my_dict_1 и my_dict_2.
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},

my_dict_1 = {"name": "Greg", "age": 29, "job": "SMM", "works": ["CSS", "PHP"]}
my_dict_2 = {"name": "Bob", "hobby": "snowboarding", "work": "CSS", "age": 34}

new_dict = {}
for key_1, value_1 in my_dict_1.items():
    for key_2, value_2 in my_dict_2.items():
        if key_1 == key_2:
            union_value = my_dict_1[key_1], my_dict_2[key_1]
            new_dict[key_1] = list(union_value)
        elif key_1 not in my_dict_2:
            new_dict[key_1] = value_1
        elif key_2 not in my_dict_1:
            new_dict[key_2] = value_2

print(new_dict)

#####################################################
## подумать как сделать choice из словаря

AB = {"A": (random.randint(-10, 10),
            random.randint(-10, 10),
            random.randint(-10, 10)),
      "B": (random.randint(-10, 10),
            random.randint(-10, 10),
            random.randint(-10, 10)),
      }
print(AB)
print(random.choice(list(AB.values())))
