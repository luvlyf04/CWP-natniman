#!/usr/bin/env python3
import sys

if len(sys.argv) > 1:

    for arg in sys.argv[1:]:
        #Check if the argument ends with "ism"
        match arg.endswith("ism"):
            case False:
                print(arg + "ism")
            case True:
                pass
else:
    print("none")