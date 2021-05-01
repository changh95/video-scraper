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

    extensions = [".mp4", ".mkv"]
    path_binary = os.path.join(".", "python_venv", "Scripts")
    if os.name == 'posix':
        path_binary = os.path.join(path_binary, "youtube-dl")

    if os.name == 'nt':
        path_binary = os.path.join(path_binary, "youtube-dl.exe")

    path_file = os.path.join(".", "index-index")

    for elem in lst:
        if os.name == 'posix':
            os.system(path_binary + " " + elem[1])
        
        if os.name == 'nt':
            os.system(path_binary + " " + elem[1])

        for ext in extensions:
            path_file += ext
            if os.path.isfile(path_file):
                os.rename(path_file, elem[0] + ext)


if __name__ == "__main__":
    main()
