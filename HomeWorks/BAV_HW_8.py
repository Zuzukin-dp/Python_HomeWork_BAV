# 1. Считать данные из файла domains.txt
# Названия интернет доменов сохранить их в виде списка строк (названия сохранить без точки).

with open("/home/bav/python/introPython_BAV/HomeWorks/domains.txt", "r") as domain_txt:
    domain_list = []
    for domain_val in domain_txt:
        domain_val = domain_val.replace(".", "")
        domain_list.append(domain_val.strip())
# print(domain_list)

# with open("/home/bav/python/introPython_BAV/HomeWorks/domains_2.txt", "w") as domain_2_txt:
#     domain_2_txt.writelines("\n".join(domain_list))

#####################################################
# 2. Считать данные из файла names.txt и сохранить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.

with open("/home/bav/python/introPython_BAV/HomeWorks/names.txt", "r") as names_txt:
    names_list = []
    for s_name in names_txt:
        s_name = s_name.split()
        names_list.append(s_name[1])
    # print(names_list)

# with open("/home/bav/python/introPython_BAV/HomeWorks/names_2.txt", "w") as names_2_txt:
#     names_2_txt.writelines("\n".join(names_list))

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

import random
import string


def generate_server_name(min_len=5, max_len=7):
    # srv_name = "".join(random.choice(list(string.ascii_lowercase)) for _ in range(random.randint(5, 7)))
    rdm_idx = string.ascii_lowercase
    srv_name = [random.choice(rdm_idx) for _ in range(random.randint(min_len, max_len))]
    srv_name = "".join(srv_name)
    return srv_name


def generate_random_number(min_num=100, max_num=999):
    rdm_number = random.randint(min_num, max_num)
    return rdm_number


def domains_from_file_list(domains, wrk_path="HomeWorks"):
    with open(f"{domains}.txt", "r") as domain_txt:
        # domain_list = [s_domain.strip().split(".")[-1] for s_domain in domain_txt]
        for domain_val in domain_txt:
            domain_val = domain_val.split(".")[-1]
            domain_list.append(domain_val.strip())
        rdm_domain = random.choice(domain_list)
        return rdm_domain


def names_from_file_list(names, wrk_path="HomeWorks"):
    with open(f"{names}.txt", "r") as names_txt:
        # names_list = [s_name[1].split() for s_name in names_txt]
        names_list = []
        for s_name in names_txt:
            s_name = s_name.split()
            names_list.append(s_name[1])
        rdm_name = random.choice(names_list)
        return rdm_name


def generate_email_address(domains, names):
    names_ff = names_from_file_list(names)
    domains_ff = domains_from_file_list(domains)
    rdm_num = generate_random_number()
    rdm_srv = generate_server_name()

    gen_email = f"{names_ff}.{rdm_num}@{rdm_srv}.{domains_ff}"
    return gen_email


domain, names = "domains", "names"
e_mail = generate_email_address(domain, names)
print(e_mail)

#####################################################
