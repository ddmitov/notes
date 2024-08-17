#!/usr/bin/env python3

# List to string:
item_list = []

string_from_list = ','.join(map(str, item_list))

# List to list of lists:
original_list = []

def batch_generator(item_list, items_per_batch):
    for item in range(0, len(item_list), items_per_batch):
        yield item_list[item:item + items_per_batch]

items_per_batch = 100

items_batch_list = list(
    batch_generator(
        original_list,
        items_per_batch
    )
)

# Sorted list using a custom sorting function:
original_list = []

def list_sorter(item_name):
    return_value = None

    if 'CRITERION_02' in item_name:
        return_value = 1

    if 'CRITERION_01' in item_name:
        return_value = 2

    return return_value

sorted_list = sorted(
    original_list,
    key=list_sorter
)

# Sorted unique list of dictionaries:
original_list = []

unique_list_of_dictionaries = list(
    map(
        dict, set(
            tuple(sorted(value)) for key, value in original_list.items()
        )
    )
)
