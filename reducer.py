#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys

current_vehicle = None
current_count = 0
vehicle = None

for line in sys.stdin:
    line = line.strip()

    vehicle, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if current_vehicle == vehicle:
        current_count += count
    else:
        if current_vehicle:
            # write result to STDOUT
            print('%s\t%s' % (current_vehicle, current_count))
        current_count = count
        current_vehicle = vehicle

# do not forget to output the last word if needed!
if current_vehicle == vehicle:
    print('%s\t%s' % (current_vehicle, current_count))