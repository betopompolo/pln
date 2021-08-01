from n_grams import n_gram

if __name__ == '__main__':
    sentence = 'this is a foo bar sentences and i want to ngramize it'
    ngram = n_gram(sentence, 5)

    for i in ngram:
        print(i)
