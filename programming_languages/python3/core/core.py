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
