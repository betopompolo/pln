import re
from typing import Optional


def extract_from_tag(text: str, tag: str) -> Optional[str]:
    search_result = re.search(f"<{tag}>(.*?)<\/{tag}>", text)
    if search_result:
        return search_result.group(1)
