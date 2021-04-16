import argparse
import csv
import os
import wget
import subprocess


def dl_youtube_dl():
    if os.name == 'posix':
        os.system(
            "sudo wget https://github.com/ytdl-org/youtube-dl/releases/download/2021.04.07/youtube-dl")
        os.system("sudo chmod a+rx ./youtube-dl")

    if os.name == 'nt':
        url = "https://github.com/ytdl-org/youtube-dl/releases/download/2021.04.07/youtube-dl.exe"
        wget.download(url)


def dl_ffmpeg():
    if os.name == 'posix':
        os.system("sudo apt install -y ffmpeg")

    if os.name == 'nt':
        os.system("pip install wget")
        url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z"
        wget.download(url)


def read_csv(lst):
    f = open('video_list.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    for line in rdr:
        lst.append((line[0], line[1]))
    f.close()


def main():
    parser = argparse.ArgumentParser(
        description='Setup')
    parser.add_argument('--youtube_dl', action='store_true',
                        help='Flag to download youtube-dl')
    parser.add_argument('--ffmpeg', action='store_true',
                        help='Flag to download ffmpeg')
    args = parser.parse_args()

    if args.youtube_dl:
        dl_youtube_dl()

    if args.ffmpeg:
        dl_ffmpeg()

    lst = []
    read_csv(lst)

    if not lst:
        print("List is empty. Terminating program")

    extensions = [".mp4", ".mkv"]

    for elem in lst:
        if os.name == 'posix':
            os.system("python3 youtube-dl \"" + elem[1] + "\"")

        if os.name == 'nt':
            os.system("python youtube-dl \"" + elem[1] + "\"")

        for ext in extensions:
            filename = "index-index" + ext
            if os.path.isfile(filename):
                os.rename(filename, elem[0] + ext)


if __name__ == "__main__":
    main()
