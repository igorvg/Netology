from main import *
import pytest
import configparser
from ya_create import Yandex


@pytest.mark.parametrize(
    "stats, company",
    [({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'yandex'),
     ({'facebook': 55, 'yandex': 120, 'vk': 145, 'google': 99, 'email': 42, 'ok': 98}, 'vk'),
     ({'facebook': 155, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'facebook')]
)
def test_get_max_sale(stats, company):
    res = get_max_sales(stats)
    assert res == company


def test_get_address():
    answer = {'Solar System': {'Earth': {'Russia': {'2018-01-01': {'yandex': {'cpc': 100}}}}}}
    res = get_address()
    assert res == answer


def test_get_visits():
    answer = 6
    res = len(get_visits())
    assert res == answer


@pytest.mark.parametrize(
    "ids, unique",
    [({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}, [15, 35, 54, 98, 119, 213]),
     ({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 7, 119, 119, 15, 119],
       'user3': [213, 98, 98, 35]}, [7, 15, 35, 54, 98, 119, 213]),
     ({'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 15, 119],
       'user3': [213, 98, 98, 35, 999]}, [15, 35, 54, 98, 119, 213, 999])]
)
def test_get_unique_id(ids, unique):
    res = list(get_unique_id(ids))
    assert res == unique


def test_get_count_queries_words():
    answer = [0, 3, 4, 0]
    res = list(get_count_queries_words().values())
    assert res == answer


@pytest.fixture
def get_token_test():
    import configparser

    config = configparser.ConfigParser()
    config.read("tokens.ini")
    token = config['TOKENS']['ya_token']

    return token


@pytest.mark.parametrize(
    "folder_name, answer",
    [('test_folder', 201),
     ('test_new_folder', 201),
     ('test_folder', 409)]
)
def test_create_folder(folder_name, answer, get_token_test):
    response = create_folder(folder_name, get_token_test)
    assert response == answer
