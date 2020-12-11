#####################################################
# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.

alpha = [chr(idx) for idx in range(ord("a"), ord("a") + 15)]
my_list = ["".join(alpha)[idx: idx + 3] for idx in range(0, len("".join(alpha)), 3)]
new_list = []
for idx, str_lst in enumerate(my_list):
    if idx % 2:
        str_lst = str_lst[::-1]
    new_list.append(str_lst)
    # print(idx, str_lst)
print(my_list)
print(new_list)


#####################################################
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".

my_list = ['aabc', 'daefa', 'aghi', 'ajkl', 'mnao']
first_a_list = [str_lst for str_lst in my_list if str_lst[0] == "a"]

print(first_a_list)

#####################################################
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.

my_list = ['aabc', 'daef', 'ghi', 'ajkl', 'mnao']
new_list = [str_lst for str_lst in my_list if str_lst.count("a") > 0]

print(new_list)

#####################################################
# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.

my_list = ['abc', 1, 'def', 2, 'ghi', 3, 'jkl', 4, 'mno', 5]
new_list = [str_lst for str_lst in my_list if type(str_lst) == str]

print(new_list)

#####################################################
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.

my_str = 'abbcddeffghiijjklmno'
my_list = [idx for idx in my_str if my_str.count(idx) == 1]

print(my_list)

#####################################################
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "abcdefgghiij"
my_str_2 = "ffghhhijklmno"
my_set_1 = set(my_str_1)
my_set_2 = set(my_str_2)
enter_set = my_set_1.intersection(my_set_2)
my_list = list(enter_set)

print(my_list)

#####################################################
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.

my_str_1 = "abcdefgghiij"
my_str_2 = "ffghhijklmno"
my_list_1 = [idx1 for idx1 in my_str_1 if my_str_1.count(idx1) == 1]
my_list_2 = [idx2 for idx2 in my_str_2 if my_str_2.count(idx2) == 1]
enter_set = set(my_list_1).intersection(set(my_list_2))
my_list = list(enter_set)

print(my_list)

#####################################################
# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность

# employee = {"Имʼя": "Олекса",
#             "Прізвище": "Довбуш",
#             "Вік": "320",
#             "Адреса": {"Країна": "Україна",
#                        "Місто": "Печеніжин",
#                        "Район": "Коломийський",
#                        "Область": "Івано-Франківська"
#                        },
#             "Робота": {"Зайнятість": "Повна зайнятість",
#                        "Псада": "Ватажок опришків",
#                        "Смаколики": "All inclusive"
#                        }
#             }

duties = {"Зайнятість": "Повна зайнятість",
          "Псада": "Ватажок опришків",
          "Смаколики": "All inclusive"
          }
address = {"Країна": "Україна",
           "Місто": "Печеніжин",
           "Район": "Коломийський",
           "Область": "Івано-Франківська"
           }
employee = {"Имʼя": "Олекса",
            "Прізвище": "Довбуш",
            "Вік": "320",
            "Адреса": address,
            "Робота": duties
            }

for k_empl in employee.items():
    if not type(k_empl[1]) == dict:
        print(f"{k_empl[0]}: {k_empl[1]}")
    elif type(k_empl[1]) == dict:
        print(k_empl[0])
        for k_othr in employee[k_empl[0]]:
            print(f"   {k_othr}: {employee[k_empl[0]][k_othr]}")

#####################################################
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло

recip = {"Индигриенты)))": {
    "Коржи": {"Мука": "1 ст.",
              "Молоко сгущенное": "1 б.",
              "Яйцо": "2 шт.",
              "Сода": "0,5 ч.л."
              },
    "Крем": {"Сметана": "200 гр.",
             "Сахар": "100 гр.",
             "Ванильный сахар": "1 уп."
             },
    "Глазурь": {"Какао": "2 ст.л.",
                "Сахар": "1 ст.л.",
                "Масло": "50 гр.",
                "Молоко": "2 ст.л."
                }
}}

for ingredients in recip:
    print(ingredients)
    for composition in recip[ingredients]:
        print("  ", composition)
        # print(composition, " - ", recip[ingredients][composition])
        for cake in recip[ingredients][composition]:
            print("     ", cake, "-", recip[ingredients][composition][cake])
# print(recip)
