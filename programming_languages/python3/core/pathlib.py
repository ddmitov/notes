#!/usr/bin/env python3

from pathlib import Path

# Create a new directory with its parent directories,
# no errors if some of the parent directories exist:
Path('/directory/path',).mkdir(
    parents  = True,
    exist_ok = True
)
