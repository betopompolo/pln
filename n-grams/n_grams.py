def n_gram(text: str, n: int) -> zip:
    split = text.split(' ')
    grams = [split[i:] for i in range(n)]
    return zip(*grams)
