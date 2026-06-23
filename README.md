# YouTube Video Downloader (Python)

A simple Python-based tool for downloading YouTube videos directly from the terminal using `yt-dlp`.

## Features

* Easily download YouTube videos.
* Automatically save videos to the `video` folder.
* Supports video downloads up to **1080p** (Full HD).
* Uses `FFmpeg` to merge video and audio into a single MP4 file.
* The default quality can be adjusted to a lower or higher resolution as needed.

---

## Requirements

You must install:

* Python 3.12 or Python 3.13
* yt-dlp
* FFmpeg

> Note: Python 3.13 is recommended.

---

## Installation

### 1. Install Python

Download and install Python from the official website.

https://www.python.org/downloads/

Make sure Python is installed correctly by running:

```bash
py --version
```

or

```bash
python --version
```

---

### 2. Install yt-dlp

Open a terminal and run:

```bash
pip install yt-dlp
```

Verify the installation:

```bash
yt_dlp --version
```

---

### 3. Install FFmpeg

#### Windows (Recommended)

Run PowerShell as Administrator:

```bash
winget install Gyan.FFmpeg
```

After the installation is complete, close and reopen your terminal.

Verify the installation:

```bash
ffmpeg -version
```

---

## How to Run the Program

Navigate to the project folder.

Then run:

```bash
py generate.py
```

The program will ask for a YouTube URL.

Example:

```text
Enter YouTube URL:
https://youtu.be/xxxxxxxx
```

Downloaded videos will be automatically saved in the following folder:

```text
video/
```

---

## Video Quality Settings

The video quality settings are located in this section:

```python
opsi = {
    "format": "bestvideo[height<=1080]+bestaudio/best",
    "outtmpl": "video/%(title)s.%(ext)s",
    "merge_output_format": "mp4",
}
```

The part you can modify is:

```python
"format": "bestvideo[height<=1080]+bestaudio/best"
```

### Available Quality Options

#### 480p

```python
"format": "bestvideo[height<=480]+bestaudio/best"
```

#### 720p

```python
"format": "bestvideo[height<=720]+bestaudio/best"
```

#### 1080p (Recommended)

```python
"format": "bestvideo[height<=1080]+bestaudio/best"
```

#### 1440p (2K)

```python
"format": "bestvideo[height<=1440]+bestaudio/best"
```

#### 2160p (4K)

```python
"format": "bestvideo[height<=2160]+bestaudio/best"
```

#### Best Available Quality

```python
"format": "bestvideo+bestaudio/best"
```

> Warning: This option may download videos at very high resolutions, resulting in larger file sizes and longer download times.

---

## Notes

* Not all YouTube videos are available in 1080p, 2K, or 4K.
* If the selected quality is unavailable, `yt-dlp` will automatically download the best available quality.
* A stable internet connection is highly recommended to avoid download failures.
* FFmpeg is required when using `bestvideo+bestaudio`, since video and audio are downloaded separately and then merged into a single MP4 file.
