#!/usr/bin/env python
from __future__ import print_function, division
from ast import literal_eval

import sys

for line in sys.stdin:
    try:
        print(literal_eval(line)['user']['screen_name'])
    except:
        pass
