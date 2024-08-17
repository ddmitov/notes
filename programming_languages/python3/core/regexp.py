#!/usr/bin/env python3

import re

# Extract text using RegExp groups:
text = 'text'
regex_filter = re.compile(r"(regex-group-one)(regex-group-two)")

text_match = regex_filter.search(text)

if text_match:
    extracted_text = text_match.group(2)

# Replace text using RegExp groups and a function:
def replacement_handler(match: object) -> str:
    return 'something' + match.group(1) + 'something'


text = re.sub(
    r"(regex-group-one)",
    replacement_handler,
    text
)
