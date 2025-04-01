#!/usr/bin/env python3

# Oneliner to check the version of a Python module:
# python3 -c "import pyarrow; print(pyarrow.__version__)"

# Variable with a dynamically generated variable name:
locals()[f'{variable_name}'] = variable_value

# Get the full path of a script:
import os

script_full_path = os.path.realpath(__file__)

# Get the similarity between two sentences:
from difflib import SequenceMatcher

ratio = SequenceMatcher(
    None,
    'first sentence',
    'second sentence',
).ratio()

# Get all files in a directory recursively:
def recursive_files_lister(root_dir: str) -> List[str]:
    return [
        os.path.join(root, filename)
        for root, _, filenames in os.walk(root_dir) 
        for filename in filenames
    ]
