from dataset_parser import load_dataset, extract_from_tag

if __name__ == '__main__':

    for content in load_dataset('folha94'):
        text = extract_from_tag(content, 'TEXT')
        print(text)
