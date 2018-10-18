#!/usr/bin/env python
from __future__ import print_function, division

import sys

current_output = None
counter = 1

for line in sys.stdin:
    line = line.strip()
    if line:
        if current_output is None:
            current_output = line
            continue
        if line == current_output:
            counter += 1
        else:
            print(current_output, counter)
            current_output = line
            counter = 1
print(current_output, counter)
