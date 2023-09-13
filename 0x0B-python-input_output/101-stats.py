#!/usr/bin/python3
"""
    Reads from stdin and computes metric
"""

import sys

size = 0
status_dict = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0,
               "405": 0, "500": 0}
count = 0

try:
    for line in sys.stdin:
        tok = line.split()
        if len(tok) >= 2:
            i = count
            if tok[-2] in status_dict:
                status_dict[tok[-2]] += 1
                count += 1
            try:
                size += int(tok[-1])
                if count == i:
                    count += 1
            except (IndexError, ValueError):
                if count == i:
                    continue
        if count % 10 == 0:
            print(f"File size: {size :d}")
            for key, value in sorted(status_dict.items()):
                if value > 0:
                    print(f"{key :s}: {value :d}")
    print(f"File size: {size :d}")
    for key, value in sorted(status_dict.items()):
        if value > 0:
            print(f"{key :s}: {value :d}")
except KeyboardInterrupt:
    print(f"File size: {size :d}")
    for key, value in sorted(status_dict.items()):
        if value > 0:
            print(f"{key :s}: {value :d}")
