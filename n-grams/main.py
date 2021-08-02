from dataset_parser import load_dataset, extract_from_tag, remove_punctuation, remove_linebreak
from n_grams import get_vocabulary, sum_vocabularies, word_count

if __name__ == '__main__':
    dataset_name = 'folha95'
    corpus_vocabulary = {}
    for content in load_dataset(dataset_name):
        text = extract_from_tag(content, 'TEXT')
        formatted_text = remove_linebreak(remove_punctuation(text))
        vocabulary = get_vocabulary(text)
        corpus_vocabulary = sum_vocabularies(corpus_vocabulary, vocabulary)

    print(f'word count for {dataset_name} is {word_count(corpus_vocabulary)}')
