import re
from os import listdir
from typing import Optional, List


def load_dataset(dataset_name: str) -> List[str]:
    dataset_path = f'dataset/{dataset_name}'

    for filename in listdir(dataset_path):
        with open(f'{dataset_path}/{filename}', encoding='iso-8859-1') as file:
            yield file.read()


def extract_from_tag(text: str, tag: str) -> Optional[str]:
    [start_tag, end_tag] = [f'<{tag}>', f'<\/{tag}>']
    tag_regex = f'{start_tag}([\s\S][\w\W][\d\D]*?){end_tag}'

    search_result = re.search(tag_regex, text)
    if search_result:
        return search_result.group(1).replace(start_tag, '').replace(end_tag, '')


def remove_punctuation(text: str) -> Optional[str]:
    result = re.sub(r'[^\w\s]', '', text)
    return "".join(result)
