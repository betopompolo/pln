import functools
import operator

Vocabulary = dict[str, int]


def n_gram(text: str, n: int) -> zip:
    split = text.split()
    grams = [split[i:] for i in range(n)]
    return zip(*grams)


def get_vocabulary(text: str) -> Vocabulary:
    vocabulary = {}
    for word in text.split():
        if vocabulary.get(word) is None:
            vocabulary[word] = 1
        else:
            vocabulary[word] += 1

    return vocabulary


def sum_vocabularies(v1: Vocabulary, v2: Vocabulary) -> Vocabulary:
    result = v1.copy()

    for key in v2.keys():
        if result.get(key) is None:
            result[key] = v2[key]
        else:
            result[key] += v2[key]

    return result


def word_count(v: Vocabulary) -> int:
    return functools.reduce(operator.add, v.values())
