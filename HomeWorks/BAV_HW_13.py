import random

# Основа ДЗ - ДЗ №8 https://github.com/30nt/IntroPython_18_11/blob/main/Homeworks/lesson8.txt
#
# Суть задания - сздать класс EmailGenerator
#
# 1. При инициализации класса передавать два параметра - путь к файлу domains.txt и путь к файлу names.txt
# Пример:
# email_generator = EmailGenerator("domains.txt", "names.txt")
#
# 2. Атрибуты экземпляра класса: domains и names.
# Получаются с помощью методов get_domains() и get_names().
# (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# self.domains = self.get_domains()
# self.names = self.get_names()
#
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
#
# 4. Написать метод экземпляра класса generate_email()
# (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com


class EmailGenerator:
    def __init__(self, domains_txt, names_txt):
        self.domains_txt = domains_txt
        self.names_txt = names_txt
        self.domains = self.create_domains_lst()
        self.names = self.create_names_lst()

    def __repr__(self):
        return f"len domains = {len(self.domains)}, len names = {len(self.names)}"

    def create_domains_lst(self):
        with open(self.domains_txt, "r") as domain_txt:
            domain_list = [s_domain.strip().split(".")[-1] for s_domain in domain_txt]
            return domain_list

    def create_names_lst(self):
        with open(self.names_txt, "r") as names_txt:
            names_list = [s_name.split()[1] for s_name in names_txt]
            return names_list

    def get_domain_from_list(self):
        rdm_domain = random.choice(self.domains)
        return rdm_domain

    def get_name_from_list(self):
        rdm_name = random.choice(self.names)
        return rdm_name

    @staticmethod
    def generate_server_name(min_len, max_len):
        alpha = [chr(idx) for idx in range(ord("a"), ord("z"))]
        srv_name = [random.choice(alpha) for _ in range(random.randint(min_len, max_len))]
        return "".join(srv_name)

    @staticmethod
    def generate_random_number(min_num, max_num):
        rdm_number = random.randint(min_num, max_num)
        return rdm_number

    def generate_email_address(self, min_num=100, max_num=999, min_len=5, max_len=7):
        names_ff = self.get_name_from_list()
        domains_ff = self.get_domain_from_list()
        rdm_num = self.generate_random_number(min_num, max_num)
        rdm_srv = self.generate_server_name(min_len, max_len)
        return f"{names_ff}.{rdm_num}@{rdm_srv}.{domains_ff}"


pth_domains = "/home/bav/python/introPython_BAV/HomeWorks/domains.txt"
pth_names = "/home/bav/python/introPython_BAV/HomeWorks/names.txt"

email_generator = EmailGenerator(pth_domains, pth_names)
#########################################################
# 3. При выводе на печать экземпляра класса вывести количество элементов в атрибутах domains и names
# Пример:
# print(email_generator)
# >>>len domains = 8, len names = 34
print(email_generator)

#########################################################
# 4. Написать метод экземпляра класса generate_email()
# (описание и реализацию нужно взять из ДЗ №8)
# Пример:
# email = email_generator.generate_email()
# print(email)
# >>>miller.249@sgdyyur.com
email = email_generator.generate_email_address()
print(email)
