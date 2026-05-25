import yt_dlp

def download_video(url):

    ydl_opts = {
        "format":
        "bestvideo+bestaudio"
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        ydl.download([url])
