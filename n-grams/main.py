from dataset_parser import load_dataset, extract_from_tag, tag_sentences, remove_symbols, \
    remove_linebreak, format_date, add_unknown_tags
from n_grams import NGramModel
from progress.bar import Bar

if __name__ == '__main__':
    ngram_model = NGramModel()

    loading_bar = Bar('Training ngram model', max=365)
    for content in load_dataset('folha95'):
        text = extract_from_tag(content, 'TEXT')
        formatted_text = add_unknown_tags(tag_sentences(remove_symbols(remove_linebreak(text)))).lower()
        ngram_model.update_train(formatted_text)
        loading_bar.next()
    loading_bar.finish()

    perplexity_results: dict[str, int] = {}
    for content in load_dataset('folha94'):
        text = extract_from_tag(content, 'TEXT')
        date = format_date(extract_from_tag(content, 'DATE')[:6])
        formatted_text = tag_sentences(remove_symbols(remove_linebreak(text))).lower()
        perplexity_results[date] = ngram_model.perplexity(formatted_text)

    print(perplexity_results)
