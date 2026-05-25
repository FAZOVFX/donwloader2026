import yt_dlp


def search_youtube(query):

    ydl_opts = {
        "quiet": True,
        "extract_flat": True
    }

    with yt_dlp.YoutubeDL(
        ydl_opts
    ) as ydl:

        result = ydl.extract_info(
            f"ytsearch5:{query}",
            download=False
        )

    return result["entries"]
