import functools
import operator

import numpy as np
import pandas as pandas

from dataset_parser import Tags

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


class NGramModel:
    def __init__(self):
        self.trigram_count: NGramCount = {}
        self.bigram_count: NGramCount = {}
        self.unigram_count: NGramCount = {}

    def update_train(self, text: str):
        trigram = n_gram(text, 3)
        bigram = n_gram(text, 2)
        unigram = n_gram(text, 1)

        self.trigram_count = sum_count(self.trigram_count, count(trigram))
        self.bigram_count = sum_count(self.bigram_count, count(bigram))
        self.unigram_count = sum_count(self.unigram_count, count(unigram))

    def perplexity(self, text: str):
        vocabulary = self.unigram_count

        formatted_text = ' '.join([t if (t,) in vocabulary else Tags.Unknown for t in text.split()])

        trigram_count = count(n_gram(formatted_text, 3))
        bigram_count = count(n_gram(formatted_text, 2))
        unigram_count = count(n_gram(formatted_text, 1))

        total = word_count(vocabulary)
        p_sum = 0
        i = 0

        for trigram, bigram, unigram in zip(trigram_count, bigram_count, unigram_count):
            try:
                p3 = trigram_count[trigram] / self.bigram_count[bigram]
            except KeyError:
                p3 = 0
            try:
                p2 = bigram_count[bigram] / vocabulary[unigram]
            except KeyError:
                p2 = 0
            p1 = unigram_count[unigram] / total

            p_sum += np.log2(p1 + p2 + p3)
            i += 1

        p_total = pow(p_sum, 2)

        perplexity = 1 / p_total ** (1 / i)
        return perplexity


def to_df(ngc: NGramCount):
    ngc_dict = [[str(key), ngc[key]] for key in ngc.keys()]
    df = pandas.DataFrame(ngc_dict, columns=['key', 'value'])
    return df
