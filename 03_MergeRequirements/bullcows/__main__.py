import textdistance
import typing as tp
from random import choice
import requests
import sys


def bullcows(guess: str, secret: str):
    bull = textdistance.hamming.similarity(guess, secret)
    return bull, len(set(guess).intersection(set(secret))) - bull


def gameplay(ask: tp.Callable, inform: tp.Callable, words: list) -> int:
    secret = choice(words)
    count_attempt = 0
    while True:
        count_attempt += 1
        word = ask("Введите слово: ", words)
        bull, cow = bullcows(word, secret)
        inform('Быки: {}, Коровы: {}', bull, cow)
        if word == secret:
            break
    return count_attempt


def _default_ask_(query: str, valid: list = None):
    while True:
        if valid is None:
            word = input(query)
            return word
        else:
            word = input(f'{query}')
            if word in valid:
                return word


def _default_inform_(query: str, *args):
    print(query.format(*args))


def _filter_words_(words: list, length: int):
    return [word for word in words if len(word) == length]


def _try_local_parse_(place: str, length: int):
    try:
        with open(place, 'r') as file:
            return _filter_words_(file.read().split('\n'), length)
    except:
        return []


def _try_download_(place: str, length: int):
    try:
        data = requests.get(place).text
        return _filter_words_(data.split('\n'), length)
    except:
        return []


def _get_dict_(place: str, length: int):
    dct = _try_download_(place, length)
    if dct:
        return dct
    return _try_local_parse_(place, length)


if __name__ == '__main__':
    dictionary, length = sys.argv[1], 5
    if len(sys.argv) > 2:
        length = int(sys.argv[2])
    
    gameplay(_default_ask_, _default_inform_, _get_dict_(dictionary, length))
