#####################################################
# 1. Дано целое число (int). Определить сколько нулей в этом числе.

value = 879517390001232398795001759000151930000000
my_result = str(value).count('0')
print(my_result)

# fnd_simb = '0'
# my_result = str(value).count(fnd_simb)
# print(my_result)

#####################################################
# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.

value = 879517390001232398795001759000151930000000
count = 0

while value % 10 == 0:
    count += 1
    value //= 10
print(count)

#####################################################
# 3a. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = [1, 6, 2, 7, 3]
my_list_2 = [8, 4, 9, 5, 10]
my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

# for idx_1 in range(len(my_list_1)):
#     if not idx_1 % 2:
#         my_result.append(my_list_1[idx_1])
# for idx_2 in range(len(my_list_2)):
#     if idx_2 % 2:
#         my_result.append(my_list_2[idx_2])
# print(my_result)

# my_list_1 = [1, 6, 2, 7, 3]
# my_list_2 = [8, 4, 9, 5, 10]
# new_list_1 = my_list_1[::2]
# new_list_2 = my_list_2[1::2]
# my_result = new_list_1 + new_list_2
# print(my_result)

#####################################################
# 3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
# вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
# my_list_1 = [1,2,3,4,5], my_list_2 = [10, 15, 20, 25] -> my_result [2, 4, 15, 25]
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_2 = [11, 13, 12, 14, 16, 15, 17, 18, 19]
my_result = []

my_list_1 = [int(even) for even in my_list_1 if not even % 2]
my_list_2 = [int(not_even) for not_even in my_list_2 if not_even % 2]
my_result.extend(my_list_1 + my_list_2)

print(my_result)

# for elm_1 in my_list_1:
#     if not elm_1 % 2:
#         my_result.append(elm_1)
# for elm_2 in my_list_2:
#     if elm_2 % 2:
#         my_result.append(elm_2)
# print(my_result)

#####################################################
# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [9, 1, 2, 3, 4, 5, 6, 7, 8]
new_list = my_list[1:]
new_list.append(my_list[0])
print(new_list)

#####################################################
# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = [9, 1, 2, 3, 4, 5, 6, 7, 8]
my_list.append(my_list.pop(0))
print(my_list)

#####################################################
# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133.

value = "43 больше чем 34 но меньше чем 56"
num = [int(num) for num in value.split(" ") if num.isdigit()]
sum_num = sum(num)
print(sum_num)

# print(value.split())
# print(num)

# num = []
# for num_str in value.split(" "):
#     if num_str.isdigit():
#         num.append(int(num_str))
# sum_num = sum(num)
# print(sum_num)
# print(value.split())
# print(num)

#####################################################
# 7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']

my_str = 'abcdfghijkl'
my_str = my_str if not len(my_str) % 2 else my_str + "_"
my_list = [my_str[index:index+2] for index in range(0, len(my_str), 2)]
print(my_list)

# my_list = []
# for index in range(0, len(my_str), 2):
#     my_list.append(my_str[index:index + 2])
# print(my_list)

# print(my_str)
# print(len(my_str))

#####################################################
# 8. Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить часть строки между этими символами.
# my_str = "My_long str", l_limit = "o", r_limit = "t" -> sub_str = "ng s"

alpha = [chr(index) for index in range(ord("a"), ord("a") + 10)]
my_str = "".join(alpha)
l_limit = "c"
r_limit = "g"

btw_chr = [btw_chr for btw_chr in my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]]
sub_str = "".join(btw_chr)
print(my_str)
print(sub_str)

# sub_str = ''
# for btw_chr in my_str[my_str.find(l_limit) + 1:my_str.find(r_limit)]:
#     sub_str += str(btw_chr)
# print(my_str)
# print(sub_str)

#####################################################
# 9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"

btw_chr = [btw_chr for btw_chr in my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]]
sub_str = "".join(btw_chr)
print(my_str)
print(sub_str)

# sub_str = ''
# for btw_chr in my_str[my_str.find(l_limit) + 1:my_str.rfind(r_limit)]:
#     sub_str += str(btw_chr)
# print(my_str)
# print(sub_str)

#####################################################
# 10. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_num_list = [2, 4, 1, 5, 3, 9, 0, 7, 1, 1, 6]
count = 0

for element in range(1, len(my_num_list)-1):
    if my_num_list[element] > my_num_list[element - 1] + my_num_list[(element + 1) % len(my_num_list)]:
        count += 1
print("Ответ: Коичество эементов - ", count)

# for element in range(1, len(my_num_list)-1):
#     if my_num_list[element] > my_num_list[element - 1] + my_num_list[(element + 1) % len(my_num_list)]:
#         elm = my_num_list[element]
#         bef_elm = my_num_list[element - 1]
#         aft_elm = my_num_list[(element + 1) % len(my_num_list)]
#         count += 1
#         print(f"Дя элемента - {elm}, соседями былли {bef_elm} и {aft_elm}")
# print("Ответ: Коичество эементов - ", count)
#####################################################
