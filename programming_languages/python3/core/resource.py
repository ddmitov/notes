#!/usr/bin/env python3

import resource

memory_usage_megabytes = round(
    (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024),
    2
)

memory_usage_gigabytes = round((memory_usage_megabytes / 1024), 2)
