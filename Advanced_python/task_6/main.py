from ya_create import Yandex
import configparser


# Task 1
def get_visits():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    sorted_geo_logs = []
    for visit in geo_logs:
        country = list(visit.values())[0][1]
        if country == 'Россия':
            sorted_geo_logs.append(visit)
    return sorted_geo_logs


# Task 2
def get_unique_id(ids):
    unique_id = []
    for key, val in ids.items():
        unique_id.extend(val)
    unique_id = list(set(unique_id))
    unique_id.sort()
    return unique_id


# Task 3
def get_count_queries_words():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    len_queries = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }
    for q in queries:
        len_querie = len(q.split())
        len_queries[len_querie] += 1
    return len_queries


# Task 4
def get_max_sales(stats):
    max_sales = max(stats.items(), key=lambda x: x[1])
    return max_sales[0]


# Task 5
def get_address():
    any_list = ['Solar System', 'Earth', 'Russia', '2018-01-01', 'yandex', 'cpc', 100]
    key = any_list.pop(-2)
    val = any_list.pop(-1)
    any_dict = {key: val}
    while len(any_list) != 0:
        key = any_list.pop(-1)
        mid_dict = any_dict.copy()
        any_dict.clear()
        any_dict[key] = mid_dict
    return any_dict


def get_token():
    config = configparser.ConfigParser()
    config.read("tokens.ini")
    token = config['TOKENS']['ya_token']

    return token


def create_folder(folder_name, token):
    yandex = Yandex(token)
    response = yandex.get_upload_link(folder_name)
    print(response)
    return response


if __name__ == '__main__':

    sorted_geo_logs = get_visits()
    for visit in sorted_geo_logs:
        print(visit)
    print()

    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}
    unique_id = get_unique_id(ids)
    print(*sorted(unique_id))
    print()

    querie_words = get_count_queries_words()

    print(f'''поисковых запросов из:
    одного слова - {querie_words[1]}
    двух слов - {querie_words[2]}
    трёх слов - {querie_words[3]}
    четырёх слов - {querie_words[4]}''')
    print()

    stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    print(get_max_sales(stats))
    print()

    print(get_address())
    print()

    token = get_token()
    folder = 'newfolder'
    print(create_folder(folder, token))