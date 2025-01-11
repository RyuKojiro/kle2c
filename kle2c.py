#!/usr/bin/env python3

import json
import os
import argparse

parser = argparse.ArgumentParser(description='Convert keyboard-layout-editor.com JSON to a C structure in a header.')
parser.add_argument('files', type=str, nargs='+',
                    help='files to convert')

args = parser.parse_args()


def keyName(kle):
    if "\n" in key:
        return key.split("\n")[1].lower()

    return key.lower()

for arg in args.files:
    with open(arg) as fp:
        basename = os.path.splitext(os.path.basename(arg))[0]
        basename = basename.replace("-", "_");
        j = json.load(fp)


        ROW_MAX = len(j)
        COL_MAX = max([len(row) for row in j])

        print("#define COL_MAX ", COL_MAX)
        print("#define ROW_MAX ", ROW_MAX)
        print()
        print("typedef unsigned int keymatrix[ROW_MAX][COL_MAX];")
        print()
        print("const keymatrix layer1 = {")
        for row in j:
            print("\t{", end='')
            for key in row:
                if type(key) is not dict:
                    print("'", end='')
                    print(keyName(key), end='')
                    print("', ", end='')
            print("},")
        print("};")
