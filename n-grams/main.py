from dataset_parser import load_dataset, extract_from_tag, tag_sentences, remove_symbols, \
    remove_linebreak, Tags
from n_grams import NGramModel

if __name__ == '__main__':
    dataset_name = 'folha95'
    ngram_model = NGramModel()

    for content in load_dataset(dataset_name):
        date = extract_from_tag(content, 'DATE')[:6]
        text = extract_from_tag(content, 'TEXT')
        formatted_text = tag_sentences(remove_symbols(remove_linebreak(text))).lower()
        ngram_model.update_train(formatted_text)

    r1 = ngram_model.perplexity(
        f'{Tags.StartOfSentence} you better watch the dog that bring the bone {Tags.EndOfSentence}')
    r2 = ngram_model.perplexity(
        f'{Tags.StartOfSentence} novo comandante do barco brasil fernando henrique cardoso {Tags.EndOfSentence}')

    print(f'from model {r2}\n-------\noutside model {r1}')
