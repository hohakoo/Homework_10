import json
import re



# Дано: data.json - файл с данными о некоторых математиках прошлого.
# 1. Условие: Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.


def read_json(my_data = "data.json"):
    with open(my_data, "r", encoding="UTF-8") as json_file:
        data = json.load(json_file)
    return data


# 2. Написать "функцию сортировки" данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
def sort_by_surname(item: dict) -> str:
    surname = item["name"].split()[-1]
    return surname


sorted_by_surnames = sorted(read_json(), key=sort_by_surname)


# 3. Написать функцию сортировки по количеству слов в поле "text".


def sort_by_number_of_words_in_text(the_dict):
    words = the_dict["text"]
    return len(words.split()), words


sorted_by_number_of_words = sorted(read_json(), key=sort_by_number_of_words_in_text)
# 4. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.


def sort_by_year(the_dict):
    years_of_life = the_dict["years"]
    bc = True if re.findall(r"BC", years_of_life) != [] else False
    year_of_death = "".join(re.findall(r"[0-9]", years_of_life.split("–")[-1]))
    if bc:
        year_of_death = "-" + year_of_death
    return int(year_of_death)


sorted_by_year = sorted(read_json(), key=sort_by_year)
