import textdistance
import typing as tp
from random import choice


def bullcows(guess: str, secret: str):
    bull = textdistance.hamming.similarity(guess, secret)
    return bull, len(set(guess).intersection(set(secret))) - bull


def gameplay(ask: tp.Callable, inform: Callable, words: list[str]) -> int:
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


if __name__ == '__main__':
    gameplay(input, print, ['abc, bcd, cde, edf, dfg'])