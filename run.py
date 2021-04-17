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

if args.setup:
    if os.name == 'posix':
        os.system("chmod u+x ./scripts/setup.sh")
        os.system("./scripts/setup.sh")

    if os.name == 'nt':
        print("I need to implement this")  # TODO

os.system("python3 ./scripts/main.py")
