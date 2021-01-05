import json
import re
# Задания
# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
# 4. Написать функцию сортировки по количеству слов в поле "text"


# 1. Функция, считывает данные из файла. Параметр функции - имя файла.
def read_json(filename):
    """ Функция, считывает данные из файла. Параметр функции - имя файла. """
    with open(filename, "r", encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data


# 2. Функция сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
def key_sort_by_last_name(obj_dict):
    """ Функция сортировки данных по ФАМИЛИИ в поле name (у тех у кого она есть). """
    last_name = re.findall(r'[A-Za-z]+', obj_dict["name"])
    d_date = last_name[-1]
    return str(d_date)


# 3. Функция сортировки по дате смерти из поля "years", с учетом дат до н.э.
def key_sort_by_years(obj_dict):
    """ Функция сортировки по дате смерти из поля years, с учетом дат до н.э. """
    l_years = re.findall(r'[0-9]+', obj_dict["years"])
    death_date = -int(l_years[-1]) if "BC" in obj_dict["years"] else int(l_years[-1])
    return death_date


# 4. Функция сортировки по количеству слов в поле "text"
def key_sort_by_quantity_words(obj_dict):
    """ Функция сортировки по количеству слов в поле text """
    words = obj_dict["text"].split()
    return len(words)


dict_json = read_json("data.json")

sort_by_name = sorted(dict_json, key=key_sort_by_last_name)
print(sort_by_name)
sort_by_words = sorted(dict_json, key=key_sort_by_quantity_words)
print(sort_by_words)
sort_by_years = sorted(dict_json, key=key_sort_by_years)
print(sort_by_years)


# # Функция сохраняет результат сортировки в файл.
# def write_json_file(filename, sort_by):
#     dct_json = read_json("data.json")
#     with open(filename, "w", encoding="utf-8") as test_json:
#         sort_dict = sorted(dct_json, key=sort_by)
#         json.dump(sort_dict, test_json, ensure_ascii=False, indent=2)
#
#
# write_json_file("/home/bav/python/introPython_BAV/HomeWorks/sort_by_last_name_data.json", key_sort_by_last_name)
# write_json_file("/home/bav/python/introPython_BAV/HomeWorks/sort_by_len_data.json", key_sort_by_quantity_words)
# write_json_file("/home/bav/python/introPython_BAV/HomeWorks/sort_by_years_data.json", key_sort_by_years)
