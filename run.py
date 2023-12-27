# @file      run.py
# @author    Hyunggi Chang     [github:changh95]
#
# Copyright (c) 2021 Hyunggi Chang, all rights reserved

import os
import argparse

parser = argparse.ArgumentParser(description='Setup')
parser.add_argument('--setup', action='store_true', help='Set this flag if running for the first time')
args = parser.parse_args()

setup_script_path = os.path.join('.', 'scripts', 'setup.sh')
main_script_path = os.path.join('.', 'scripts', 'main.py')

if os.name == 'posix' or os.name == 'darwin':
    if args.setup:
        os.system(f'chmod u+x {setup_script_path}')
        os.system(f'{setup_script_path}')
    os.system(f'python3 {main_script_path}')

elif os.name == 'nt':
    if args.setup:
        raise NotImplementedError('TODO')
    os.system(f'python {main_script_path}')

else:
    raise NotImplementedError
