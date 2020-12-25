import random
import string

# 1. Считать данные из файла domains.txt
# Названия интернет доменов сохранить их в виде списка строк (названия сохранить без точки).

with open("/home/bav/python/introPython_BAV/HomeWorks/domains.txt", "r") as domain_txt:
    domains_list = []
    for domain_val in domain_txt:
        domain_val = domain_val.split(".")[-1]
        domains_list.append(domain_val.strip())

#####################################################
# 2. Считать данные из файла names.txt и сохранить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

with open("/home/bav/python/introPython_BAV/HomeWorks/names.txt", "r") as names_txt:
    names_list = []
    for s_name in names_txt:
        s_name = s_name.split()
        names_list.append(s_name[1])

#####################################################
# 3. Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать из списков, полученных в задачах 1 и 2 и переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
#
# Пример вызова функции:
# e_mail = create_email(domains, names)
# print(e_mail)
#
# >>>miller.249@sgdyyur.com


def domains_from_file_list(domains):
    rdm_domain = random.choice(domains)
    return rdm_domain


def names_from_file_list(names):
    rdm_name = random.choice(names)
    return rdm_name


def generate_server_name(min_len, max_len):
    srv_name = "".join(random.choice(list(string.ascii_lowercase)) for _ in range(random.randint(min_len, max_len)))
    return srv_name


def generate_random_number(min_num, max_num):
    rdm_number = random.randint(min_num, max_num)
    return rdm_number


def generate_email_address(domains, names, min_num=100, max_num=999, min_len=5, max_len=7):
    names_ff = names_from_file_list(names)
    domains_ff = domains_from_file_list(domains)
    rdm_num = generate_random_number(min_num, max_num)
    rdm_srv = generate_server_name(min_len, max_len)
    return f"{names_ff}.{rdm_num}@{rdm_srv}.{domains_ff}"


e_mail = generate_email_address(domains_list, names_list)
print(e_mail)
#####################################################
