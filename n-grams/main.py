from dataset_parser import extract_from_tag

if __name__ == '__main__':
    sentence = 'this is the real text</text> a foo bar sentences and i want to ngramize it'
    result = extract_from_tag(sentence, 'text')
    print(result)

