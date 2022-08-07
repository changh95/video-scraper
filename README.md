# video-scraper

## Features

- **Video downloader with just a single command**.
  - [youtube-dl](https://github.com/ytdl-org/youtube-dl) is used to download videos
  - A .csv file is used to manage what videos to download.

![](./images/demo.gif)

## Example uses

- Downloading lecture videos from Youtube
- Downloading music videos from Youtube
- Downloading presentation videos from online academic conferences

## How to use

> Works for Windows / MacOS / Linux! :smile_cat:
> 
> If you are using `python` alias instead of `python3`, use `python` command instead of `python3` (Most likely if you are using Windows)

```bash
# Fill the 'video_list.csv' before running the command.
# First column of the csv file should be 'video name'
# Second column of the csv file should be 'video url'

python3 ./run.py --setup
```

## Downloading video from other websites

- If you are downloading a video from a website that is not officially supported by [youtube-dl](https://github.com/ytdl-org/youtube-dl)...
  - Get the streaming url by using [Video Downloadhelper](https://chrome.google.com/webstore/detail/video-downloadhelper/lmjnegcaeklhafolokijcfjliaokphfk?hl=ko).
  - Paste the streaming url onto the `video_list.csv`

![](./images/video_download_helper.gif)

## License / Legal issues

- I strongly recommend using this software **ONLY to download videos for PERSONAL USE**.
- I am not responsible for any legal issues caused by copyright violations.
  - For example...
    - Sharing the videos without original author's contents
    - Profitting from the videos you downloaded
    - Downloading the videos from the websites where it's not allowed.
