#! /usr/bin/env python3
import sys

if len(sys.argv) > 2:
    for agv in sys.argv[1:]:
        print(agv)
else:
    print("none")