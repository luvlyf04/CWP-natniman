#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:
    print("parameters:", len(sys.argv) - 1)

    #Loop through each argument ex: ["Game", "of", "Thrones"]
    for arg in sys.argv[1:]:
        print(f"{arg}: {len(arg)}")
else:
    print("none")