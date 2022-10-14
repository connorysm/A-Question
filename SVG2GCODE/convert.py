#!/usr/bin/env python

from svg2gcode import main
import sys
# from config import *


if __name__ == "__main__":

    if len(sys.argv) < 3:
        print("usage: python convert.py source.svg destination.gcode")
        sys.exit()

    source = sys.argv[1]
    target = sys.argv[2]

    print("converting!")

    print(source, target)

    main(source, target)

    print("done!")