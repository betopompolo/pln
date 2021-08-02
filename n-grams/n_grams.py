import functools
import operator

NGram = zip
NGramCount = dict[NGram, int]


def n_gram(text: str, n: int) -> NGram:
    split = text.split()
    grams = [split[i:] for i in range(n)]
    return zip(*grams)


def count(ngram: NGram) -> NGramCount:
    ngram_count = {}
    for data in ngram:
        if data in ngram_count:
            ngram_count[data] += 1
        else:
            ngram_count[data] = 1

    return ngram_count


def sum_count(v1: NGramCount, v2: NGramCount) -> NGramCount:
    result = v1.copy()

    for key in v2.keys():
        if result.get(key) is None:
            result[key] = v2[key]
        else:
            result[key] += v2[key]

    return result


def word_count(ngram_count: NGramCount) -> int:
    if any(len(list(key)) != 1 for key in ngram_count.keys()):
        raise AttributeError('word_count accepts unigrams only')
    return functools.reduce(operator.add, ngram_count.values())
