#!/bin/sh

echo "Creating a list of all JPEG files in the current folder..."

declare -a JPEG_FILES
JPEG_FILES=($(ls *.jpg))

if [ "${#JPEG_FILES[@]}" = 0 ]; then
    echo "There are no JPEG files in the current folder! Quitting."
    exit 1;
fi

# Tell the user how many files are going to be converted:
echo "${#JPEG_FILES[@]} files are going to be removed."

# Iteration of every element of the array JPEG_FILES:
for FILE in "${JPEG_FILES[@]}"; do
    rm -f ${FILE};
done

# Say to the user that we are ready:
echo "Removal successfull!"
