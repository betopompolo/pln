import re
from os import listdir
from typing import Optional, List


def load_dataset(dataset_name: str) -> List[str]:
    dataset = []
    dataset_path = f'dataset/{dataset_name}'

    for filename in listdir(dataset_path):
        with open(f'{dataset_path}/{filename}', encoding='iso-8859-1') as file:
            dataset.append(file.read())

    return dataset


def extract_from_tag(text: str, tag: str) -> Optional[str]:
    search_result = re.search(f"<{tag}>(.*?)<\/{tag}>", text)
    if search_result:
        return search_result.group(1)


def remove_punctuation(text: str) -> Optional[str]:
    result = re.sub(r'[^\w\s]', '', text)
    return "".join(result)
