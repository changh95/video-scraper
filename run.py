# @file      run.py
# @author    Hyunggi Chang     [github:changh95]
#
# Copyright (c) 2021 Hyunggi Chang, all rights reserved

import os
import argparse

parser = argparse.ArgumentParser(
    description='Setup')
parser.add_argument('--setup', action='store_true',
                    help='Set this flag if running for the first time')
args = parser.parse_args()

if os.name == 'posix' or os.name == 'darwin':
    if args.setup:
        os.system("chmod u+x ./scripts/setup.sh")
        os.system("./scripts/setup.sh")

    os.system("python3 ./scripts/main.py")

if os.name == 'nt':
    if args.setup:
        print("Need to develop code for this part") #TODO

    os.system("python ./scripts/main.py")
