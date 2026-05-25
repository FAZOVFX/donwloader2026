import yt_dlp
import os
import uuid

DOWNLOAD_PATH = "downloads"

os.makedirs(
    DOWNLOAD_PATH,
    exist_ok=True
)


def download_video(url):

    filename = f"{uuid.uuid4()}.mp4"

    path = os.path.join(
        DOWNLOAD_PATH,
        filename
    )

    ydl_opts = {
        "format":
        "bestvideo[height<=1080]+bestaudio/best",

        "merge_output_format":
        "mp4",

        "outtmpl":
        path,

        "quiet":
        True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        ydl.download([url])

    return path


def download_mp3(url):

    filename = f"{uuid.uuid4()}.mp3"

    path = os.path.join(
        DOWNLOAD_PATH,
        filename
    )

    ydl_opts = {
        "format":
        "bestaudio/best",

        "outtmpl":
        path,

        "postprocessors": [
            {
                "key":
                "FFmpegExtractAudio",

                "preferredcodec":
                "mp3",

                "preferredquality":
                "192"
            }
        ],

        "quiet":
        True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        ydl.download([url])

    return path
