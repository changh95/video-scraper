# @file      main.py
# @author    Hyunggi Chang     [github:changh95]
#
# Copyright (c) 2021 Hyunggi Chang, all rights reserved

import csv
import os


def read_csv(lst):
    path = os.path.join(".", "video_list.csv")
    f = open(path, 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        lst.append((line[0], line[1]))
    f.close()


def main():
    lst = []
    read_csv(lst)

    if not lst:
        print("List is empty. Terminating program")
        return

    path_binary = None
    if os.name == 'posix':
        path_binary = os.path.join(".", "python_venv", "bin", "yt-dlp")
    elif os.name == 'nt':
        path_binary = os.path.join(".", "python_venv", "Scripts", "yt-dlp.exe")
    else:
        raise NotImplementedError

    for elem in lst:
        output_name, media_url = elem
        if os.name == 'posix':
            os.system(f'{path_binary} "{media_url}" -o "{output_name}"')
        elif os.name == 'nt':
            os.system(f'{path_binary} {media_url} -o {output_name}')
        else:
            raise NotImplementedError


if __name__ == "__main__":
    main()
