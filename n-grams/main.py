from dataset_parser import load_dataset, extract_from_tag, remove_punctuation, remove_linebreak

if __name__ == '__main__':
    for content in load_dataset('folha94'):
        text = extract_from_tag(content, 'TEXT')
        text = remove_punctuation(text)
        text = remove_linebreak(text)
        print(text + '\n--------')
