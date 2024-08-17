#!/usr/bin/env python3

# Create a directory:
if not os.path.exists('directory'):
    os.makedirs('directory')

# Remove a directory:
import shutil

try:
    shutil.rmtree('directory')
except OSError as error:
    print("Error: %s - %s." % (error.filename, error.strerror))
