# YouTube Downloader

A simple Python script to download YouTube videos in MP4 format using yt-dlp.

## Features

- Downloads YouTube videos automatically in MP4 format
- Saves videos to the 'video' folder
- Uses cookies for authentication to bypass restrictions
- Includes headers and options to avoid 403 errors

## Requirements

- Python 3.x
- yt-dlp installed (`pip install yt-dlp`)
- Chrome browser (for cookie extraction, optional but recommended)

## Installation

1. Clone or download the repository.
2. Install yt-dlp:
   ```
   pip install yt-dlp
   ```
3. Ensure yt-dlp is in your PATH or update the path in `downloader.py`.

## Usage

1. Update `cookie.txt` with fresh cookies from a logged-in YouTube session in Chrome. You can use browser extensions like "Get cookies.txt" to export cookies.

2. Run the script:
   ```
   py downloader.py
   ```

3. Enter the YouTube URL when prompted. The video will be downloaded in MP4 format to the 'video' folder.

## Configuration

- **Cookie File**: `cookie.txt` - Update this with fresh cookies to avoid age-restricted or authentication errors.
- **Output Folder**: Videos are saved to the 'video' folder by default.
- **Format**: Fixed to MP4 (best quality up to 720p).

## Troubleshooting

- **403 Forbidden Error**: Update `cookie.txt` with fresh cookies from a logged-in browser session.
- **Age-Restricted Videos**: Ensure cookies are from a logged-in account that can access such content.
- **Chrome Cookie Copy Error**: Close Chrome and try again, or use manual cookie export.

## License

This project is for educational purposes only. Please respect YouTube's terms of service and copyright laws.
