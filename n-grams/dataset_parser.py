import random
import re
from os import listdir
from typing import Optional, List

sentences_regex = re.compile(r'([A-Z][^\.!?]*[\.!?])', re.M)


class Tags:
    StartOfSentence = '<s>'
    EndOfSentence = '</s>'
    Unknown = '<unk>'


def load_dataset(dataset_name: str) -> List[str]:
    dataset_path = f'dataset/{dataset_name}'

    for filename in listdir(dataset_path):
        if filename.endswith('.sgml'):
            with open(f'{dataset_path}/{filename}', encoding='iso-8859-1') as file:
                yield file.read()


def extract_from_tag(text: str, tag: str) -> Optional[str]:
    [start_tag, end_tag] = [f'<{tag}>', f'<\/{tag}>']
    tag_regex = f'{start_tag}([\s\S][\w\W][\d\D]*?){end_tag}'

    search_results = re.findall(tag_regex, text)
    if len(search_results) > 0:
        return "".join([s.replace(start_tag, '').replace(end_tag, '') for s in search_results])


def tag_sentences(text: str) -> str:
    sentences = sentences_regex.findall(text)
    tagged_sentences = [f'{Tags.StartOfSentence} {s.strip()[:-1]} {Tags.EndOfSentence} ' for s in sentences]

    return "".join(tagged_sentences)


def remove_linebreak(text: str) -> str:
    return text.replace('\n', ' ').strip()


def remove_symbols(text: str) -> str:
    return text.replace(',', '').replace(';', '')


def add_unknown_tags(text: str, tags_rate=0.01) -> str:
    split_text = text.split()
    split_text_len = len(split_text)
    unk_count = int(split_text_len * tags_rate)
    unk_indexes: list[int] = []

    while len(unk_indexes) < unk_count:
        unk_index = random.randint(0, split_text_len)
        is_tag_index = any(tag == split_text[unk_index] for tag in [Tags.StartOfSentence, Tags.EndOfSentence])

        if unk_index not in unk_indexes or is_tag_index is False:
            unk_indexes.append(unk_index)
            split_text[unk_index] = Tags.Unknown

    return " ".join(split_text)
