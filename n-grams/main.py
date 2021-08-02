import time

from dataset_parser import load_dataset, extract_from_tag, remove_linebreak, tag_sentences, remove_symbols
from n_grams import count, sum_count, word_count, n_gram, NGramCount

if __name__ == '__main__':
    start = time.time()
    dataset_name = 'folha95'
    trigram_count: NGramCount = {}
    bigram_count: NGramCount = {}
    unigram_count: NGramCount = {}

    for content in load_dataset(dataset_name):
        text = extract_from_tag(content, 'TEXT')
        formatted_text = tag_sentences(remove_symbols(remove_linebreak(text)))

        trigram = n_gram(formatted_text, 3)
        bigram = n_gram(formatted_text, 2)
        unigram = n_gram(formatted_text, 1)

        trigram_count = sum_count(trigram_count, count(trigram))
        bigram_count = sum_count(bigram_count, count(bigram))
        unigram_count = sum_count(unigram_count, count(unigram))

    print(f'word_count {word_count(unigram_count)}')
