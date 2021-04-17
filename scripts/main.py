# @file      main.py
# @author    Hyunggi Chang     [github:changh95]
#
# Copyright (c) 2021 Hyunggi Chang, all rights reserved

import csv
import os


def read_csv(lst):
    f = open('./video_list.csv', 'r', encoding='utf-8')
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

    for elem in lst:
        os.system("./python_venv/bin/youtube-dl " + elem[1])

        for ext in extensions:
            filename = "../index-index" + ext
            if os.path.isfile(filename):
                os.rename(filename, elem[0] + ext)


if __name__ == "__main__":
    main()
