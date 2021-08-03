from typing import Union

from dataset_parser import load_dataset, extract_from_tag, tag_sentences, remove_symbols, \
    remove_linebreak, format_date, add_unknown_tags
from n_grams import NGramModel, word_count
from plot import plot_results

if __name__ == '__main__':
    ngram_model = NGramModel()

    print('training...')
    for content in load_dataset('folha95'):
        text = extract_from_tag(content, 'TEXT')
        formatted_text = add_unknown_tags(tag_sentences(remove_symbols(remove_linebreak(text)))).lower()
        ngram_model.update_train(formatted_text)

    print('evaluating...')
    perplexity_results: dict[str, int] = {}
    for content in load_dataset('folha94'):
        text = extract_from_tag(content, 'TEXT')
        date = format_date(extract_from_tag(content, 'DATE')[:6])
        formatted_text = tag_sentences(remove_symbols(remove_linebreak(text))).lower()
        perplexity_results[date] = ngram_model.perplexity(formatted_text)

    lowest: Union[list[int, str], None] = None
    highest: Union[list[int, str], None] = None
    for key in perplexity_results:
        result = perplexity_results[key]

        if highest is None or result > highest[0]:
            highest = [result, key]
        if lowest is None or result < lowest[0]:
            lowest = [result, key]

    print(f'lowest {lowest}')
    print(f'highest {highest}')
    print(f'words\n\ttotal {word_count(ngram_model.unigram_count)}\n\tdistinct {len(ngram_model.unigram_count.keys())}')

    plot_results(perplexity_results)
