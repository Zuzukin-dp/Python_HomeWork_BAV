# Цель задания - создать функции, которые будут генерировать случайные данные нужного формата
# для записи в файлы разных типов.
######################################################
# Функция 1. Создает данные для записи в файл txt.
# Функция генерирует и возвращает строку случайной длинны (не менее 100 но не более 1000 символов).
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.


import random
import string
import json
import csv


def create_text_line(min_len, max_len):
    txt_list = [random.choice(list(string.ascii_lowercase)) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def create_number_line(min_len, max_len):
    txt_list = [random.choice(list(string.digits)) for _ in range(random.randint(min_len, max_len))]
    return "".join(txt_list)


def split_text_line(txt_line):
    space_count = len(txt_line) // 10
    space_index_list = []
    while len(space_index_list) < space_count:
        index = random.randint(1, len(txt_line) - 2)
        if (index not in space_index_list and
                index - 1 not in space_index_list and
                index + 1 not in space_index_list):
            space_index_list.append(index)
    for index in space_index_list:
        txt_line = txt_line[:index] + " " + txt_line[index + 1:]
    return txt_line


def replace_text_to_number(word):
    if len(word) > 5:
        return word
    else:
        return create_number_line(len(word), len(word))


def replace_first_letter(word):
    return word.capitalize()
    # return word.replace(word[0], word[0].upper(), 1)


def replace_last_letter(word):
    signs = ',.;:!?'
    if len(word) < 4:
        return word
    else:
        return word[:-1] + random.choice(signs)


def create_random_txt_data(min_len=100, max_len=1000):
    txt_line = create_text_line(min_len, max_len)
    txt_line = split_text_line(txt_line)
    new_words = []
    for word in txt_line.split():
        case = random.randint(1, 100)
        if not case % 10:
            new_word = replace_text_to_number(word)
        elif not case % 2:
            new_word = replace_first_letter(word)
        elif not case % 5:
            new_word = replace_last_letter(word)
        else:
            new_word = word
        new_words.append(new_word)
    return " ".join(new_words)


# txt_data = create_random_txt_data()
# print("TXT", txt_data)

######################################################
# Функция 2. Создает данные для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.


def generate_dict_key(quantity_keys, len_key):
    dict_key = [create_text_line(len_key, len_key) for _ in range(quantity_keys)]
    return dict_key


def random_int(min_num=-100, max_num=100):
    return random.randint(min_num, max_num)


def random_float():
    return random.random()


def random_bool():
    return bool(random.getrandbits(1))

# затрудняюсь реализоать равновероятный выбор значений
def generate_dict_value(quantity_values):
    # dict_val = [create_random_val() for _ in range(quantity_values)]
    dict_val = []
    for rdm_val in range(quantity_values):
        case = random.randint(1, 100)
        if not case % 22:
            rdm_val = random_int()
        elif not case % 12:
            rdm_val = random_float()
        elif not case % 5:
            rdm_val = random_bool()
        dict_val.append(rdm_val)
    return dict_val


def create_random_dict_js_data(min_quantity=5, max_quantity=20, len_key=5):
    quantity_key_val = random.randint(min_quantity, max_quantity)
    dict_keys = generate_dict_key(quantity_key_val, len_key)
    dict_values = generate_dict_value(quantity_key_val)
    js_dict = dict(zip(dict_keys, dict_values))
    return js_dict


# json_dict = create_random_dict_js_data()
# print("JSON", json_dict)

######################################################
# Функция 3. Создает данные для записи в файл csv.
# Создает и возвращает список длинны n внутренних списков длинны m (таблица с n строк и m столбцов).
# Числа n и m выбираются случайно в диапазоне от 3 до 10.
# В таблицу записывать значения только 0 или 1.
# Заголовка у таблицы нет.


def random_binary_digit():
    return random.getrandbits(1)


def create_sublist(len_list):
    sub_list = [random_binary_digit() for _ in range(len_list)]
    return sub_list


def create_random_list_csv_data(min_len=3, max_len=10):
    len_list = random.randint(min_len, max_len)
    len_sub_list = random.randint(min_len, max_len)
    csv_list_data = [create_sublist(len_sub_list) for _ in range(len_list)]
    # csv_list_data = [create_sublist(random.randint(min_len, max_len)) for _ in range(random.randint(min_len, max_len))]
    # для разной длинны m (количества стлбцов)
    return csv_list_data


# csv_list = create_random_list_csv_data()
# print(csv_list)

######################################################
# А теперь основное задание:
# Написать функцию generate_and_write_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) сгенерировать данные для записи и записать в данный файл.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"


def write_txt_file(filename):
    with open(filename, "w") as test_txt:
        test_txt.writelines("".join(create_random_txt_data()))


def write_json_file(filename):
    with open(filename, "w") as test_json:
        json.dump(create_random_dict_js_data(), test_json, indent=2)


def write_csv_file(filename):
    with open(filename, "w") as test_csv:
        write_data = csv.writer(test_csv, delimiter=";")
        write_data.writerows(create_random_list_csv_data())


def generate_and_write_file(filename):
    file_extension = filename.split('.')[-1]
    if file_extension == "txt":
        result = write_txt_file(filename)
    elif file_extension == "json":
        result = write_json_file(filename)
    elif file_extension == "csv":
        result = write_csv_file(filename)
    else:
        result = print("Unsupported file format")
    return result


generate_and_write_file("/home/bav/python/introPython_BAV/HomeWorks/test_data.txt")
generate_and_write_file("/home/bav/python/introPython_BAV/HomeWorks/test_data.json")
generate_and_write_file("/home/bav/python/introPython_BAV/HomeWorks/test_data.csv")

# write_txt_file("/home/bav/python/introPython_BAV/HomeWorks/test_data.txt")
# write_json_file("/home/bav/python/introPython_BAV/HomeWorks/test_data.json")
# write_csv_file("/home/bav/python/introPython_BAV/HomeWorks/test_data.csv")
