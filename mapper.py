#!/usr/bin/env python
"""mapper.py"""

import sys
import csv

reader = csv.reader(sys.stdin)
next(reader) # Skip first line
for row in reader:
    for vehicle_num in range(24, 29):
        vehicle_type = row[vehicle_num]
        if vehicle_type != "":
                print('%s\t%s' % (vehicle_type, 1))