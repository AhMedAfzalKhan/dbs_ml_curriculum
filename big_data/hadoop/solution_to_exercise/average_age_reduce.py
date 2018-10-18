#!/usr/bin/env python
from __future__ import print_function, division

import sys

age_sum = 0
counter = 1

for line in sys.stdin:
    line = line.strip()
    if line:
        try:
            counter+=1
            age_sum += float(line.strip().replace('\n',''))
        except:
            pass
print(age_sum/counter)
