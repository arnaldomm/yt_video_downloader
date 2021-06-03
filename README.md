# yt_video_downloader

* This script will download a list of videos from YouTube.
* It will filter the streams by `progressive=True` and `file_extension='mp4'`. This guarantees that the downloaded stream will be a video with embedded audio.
* From the available streams, it will pick the one with best quality, which for progressive videos (audio embedded) is up to 720p.

## Install

* Install `python3` in your system.
* In the terminal run `$ pip3 install pytube` to install the _pytube library_.

## How to use

* Add the URLs of the videos you want to download inside **_urls.txt_** by placing each URL in its own line.
* Open a terminal in the folder containing the `yt_download.py` file, and execute it with this command `$ python3 yt_download.py`.
* While the script is running, you will see in the terminal the list of videos that are downloaded. Green URLs were successfully downloaded while red URLs failed.
* After the script is done, you will find the downloaded videos inside the `./Downloads` folder.

## Authors

* **Arnaldo Moreno**

## License

This project is licensed under the MIT License.