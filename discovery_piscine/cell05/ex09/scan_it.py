#!/usr/bin/env python3
import sys
import re

if len(sys.argv) == 3:
    #Find all in the second argument that match the first argument, re.findall returns a list
    result = re.findall(sys.argv[1], sys.argv[2])

    #Print length of the result
    if len(result) > 0:
        print(len(result))
    else:
        print("none")
else:
    print("none")