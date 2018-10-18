#!/usr/bin/env python
from __future__ import print_function, division
import sys

for line in sys.stdin:
    try:
        data = line.replace('\n','').split(', ')
        print(data[0])
    except:
        pass
