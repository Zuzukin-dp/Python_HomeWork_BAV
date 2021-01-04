# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
import re
from random import randint as rdm_randint
import csv
import requests


def get_quotes_by_api():
    my_dict = {}
    params = {"method": "getQuote", "format": "json", "key": rdm_randint(0, 9999), "lang": "ru"}
    r = requests.get("http://api.forismatic.com/api/1.0/", params=params)
    quote = r.json()
    if quote["quoteAuthor"]:
        my_dict["Author"], my_dict["Quote"], my_dict["URL"] =\
            quote["quoteAuthor"], quote["quoteText"], quote["quoteLink"]
        return my_dict
    else:
        return get_quotes_by_api()


def key_sort_by_last_name(obj_dict):
    last_name = re.findall(r'[А-Яа-я]+', obj_dict["Author"])
    d_date = last_name[-1]
    return str(d_date)


def write_csv_file(list_dct, filename="pars_quotes.csv"):
    with open(filename, "w") as test_csv:
        csv_writer = csv.DictWriter(test_csv, fieldnames=["Author", "Quote", "URL"])
        csv_writer.writeheader()
        csv_writer.writerows(list_dct)


def get_list_quotes_by_api(len_list=10):
    list_quotes = [get_quotes_by_api() for _ in range(len_list)]
    list_quotes = sorted(list_quotes, key=key_sort_by_last_name)
    return write_csv_file(list_quotes)


res = get_list_quotes_by_api()
# print(res)


# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
#
# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
#
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]
#
# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.