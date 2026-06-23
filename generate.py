import os
import yt_dlp

os.makedirs("video", exist_ok=True)

url = input("Enter Youtube URL: ")

opsi = {
    "format": "bestvideo[height<=1080]+bestaudio/best",
    "outtmpl": "video/%(title)s.%(ext)s",
    "merge_output_format": "mp4",
}

try:
    with yt_dlp.YoutubeDL(opsi) as ydl:
        ydl.download([url])

    print("Download Success!")

except Exception as e:
    print(e)