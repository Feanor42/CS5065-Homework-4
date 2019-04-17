#!/usr/bin/env python
"""mapper.py"""

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.split(",")

    for vehicle_num in range(24, 29):
        vehicle_type = line[vehicle_num]
        print('%s\t%s' % (vehicle_type, 1))