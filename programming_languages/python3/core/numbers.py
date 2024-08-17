#!/usr/bin/env python3

# Division of large numbers to avoid:
# OverflowError: integer division result too large for a float
divisible = 10000000
divider = 3
result = None

try:
    result = round(
        (
            int(divisible) /
            int(divider)
        ), 3
    )
except OverflowError:
    result = round(
        (
            int(divisible) //
            int(divider)
        ), 3
    )

# Zero-filled number:
integer = 5
str(integer).zfill(4)
