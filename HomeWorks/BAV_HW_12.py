# Все пункты сделать как отдельные функции(можно создавать дополнительные вспомагательные функции)
#
# 1. Написать функцию, которая принимает в виде параметра целое число - количество цитат (см. урок 12).
# Надо получить ровно столько не повторяющихся цитат с данными и сохранить их в csv файл
# (имя файла сделать параметром по умолчанию).
# Заголовки файла:
# Author, Quote, URL. Если автор не указан, цитату не брать.
# Перед сохранением в csv, записи отсортировать по автору (в алфавитном порядке).
import re
from datetime import datetime
import json
import random
import csv
import requests


def get_quotes_by_api():
    params = {"method": "getQuote", "format": "json", "key": random.randint(0, 9999), "lang": "ru"}
    r = requests.get("http://api.forismatic.com/api/1.0/", params=params)
    quote = r.json()
    if quote["quoteAuthor"]:
        my_dict = {"Author": quote["quoteAuthor"],
                   "Quote": quote["quoteText"],
                   "URL": quote["quoteLink"]}
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


get_list_quotes_by_api()

#############################################################################################################
# 2. Дан файл authors.txt
# 2.1) написать функцию, которая считывает данные из этого файла,
# возвращая СПИСОК тех строк в которых есть полная дата, писатель и указание на его день рождения или смерти.
# Например: 26th February 1802 - Victor Hugo's birthday - author of Les Misérables.
# import re
# from datetime import datetime
# import json

def generate_list_from_txt_file(filename="authors.txt"):
    with open("authors.txt", "r") as f_txt:
        s_name = [s_name.strip() for s_name in f_txt]
        reg_exp_fdate = re.compile(r"^\d{1,2}\D{2}\s\D+\s\d{4}(.+[dD]eath|.+[bB]irthday)(.+[aA]uthor|.+[cC]reator)")
        s_name = list(filter(reg_exp_fdate.match, s_name))
        return s_name


# print(reading_txt_file())

# 2.2) Написать функцию, которая принимает список строк полученной в пункте 2.1, и возвращает список словарей
# в формате {"name": name, "date": date},
# где name это имя автора, а date - дата из строки в формате "dd/mm/yyyy" (d-день, m-месяц, y-год)
# Например [{"name": "Charles Dickens", "date": "09/06/1870"}, ...,
# {"name": "J. D. Salinger", "date": "01/01/1919"}]

def convert_date(old_date):
    ord_num = ["st", "nd", "rd", "th"]
    idx = old_date.split()
    for i in ord_num:
        if i in idx[0]:
            new_date = datetime.strptime(" ".join(idx), f"%d{i} %B %Y")
    return datetime.strftime(new_date.date(), "%d/%m/%Y")


def generate_dict_from_list(list_name=generate_list_from_txt_file()):
    my_list = []
    reg_exp_date = r"^\d{1,2}\D{2}\s\D+\s\d{4}"
    reg_exp_name = r"[^\d\s-]\D+\s[A-Z]\w+['][s]"
    for values in list_name:
        new_date = "".join(re.findall(reg_exp_date, values))
        new_name = "".join(re.findall(reg_exp_name, values))[:-2]
        new_date = convert_date(new_date)
        my_dict = {"name": new_name,
                   "date": new_date}
        my_list.append(my_dict)
    return my_list


# print(generate_dict_from_list())


# 2.3) Написать функцию, которая сохраняет результат пункта 2.2 в json файл.

def save_list_to_json_file(filename="HW_12.json"):
    with open(filename, "w", encoding="utf-8") as test_json:
        my_list_dct = generate_dict_from_list()
        json.dump(my_list_dct, test_json, ensure_ascii=False, indent=2)


save_list_to_json_file()
