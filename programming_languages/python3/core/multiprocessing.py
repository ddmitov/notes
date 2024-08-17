#!/usr/bin/env python3

import multiprocessing
import numpy as np


def process_error_callback(error: str) -> True:
    print(error, flush=True)

    return True


def batch_processor(
    process_number: int,
    batch: list
) -> list:
    return batch


def main():
    input_data = []

    cpu_count = multiprocessing.cpu_count()

    batch_list = np.array_split(
        input_data,
        cpu_count
    )

    batch_processor_arguments = [
        (
            batch_number + 1,
            batch_list[batch_number],
        ) for batch_number in range(len(batch_list))
    ]

    result_list = []

    with multiprocessing.get_context('spawn').Pool(cpu_count) as processing_pool:
        results = processing_pool.starmap_async(
            batch_processor,
            batch_processor_arguments,
            error_callback=process_error_callback
        )

        results.wait()

        result_list.extend(results.get())


if __name__ == '__main__':
    main()
