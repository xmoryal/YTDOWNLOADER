import os
import subprocess

def download_video(url, output_path='video'):
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        yt_dlp_path = r"C:\\Users\\maaaz\\AppData\\Local\\Programs\\Python\\Python313\\Scripts\\yt-dlp.exe"
        output_template = os.path.join(output_path, '%(title)s.%(ext)s')

        cookie_file = 'cookie.txt'

        base_command = [
            yt_dlp_path,
            '--cookies', cookie_file,
            '-o', output_template,
            '--user-agent',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            '--referer', 'https://www.youtube.com/',
            '--add-header', 'Accept-Language: en-US,en;q=0.9',
            '--add-header', 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            '--add-header', 'Accept-Encoding: gzip, deflate, br',
            '--add-header', 'DNT: 1',
            '--add-header', 'Connection: keep-alive',
            '--add-header', 'Upgrade-Insecure-Requests: 1',
            '--no-check-certificate',
            '--geo-bypass'
        ]

        base_command.extend(['--format', 'best[ext=mp4][height<=720]'])

        base_command.append(url)

        print("Starting download...\n")
        result = subprocess.run(base_command, capture_output=True, text=True)

        print(result.stdout)
        print(result.stderr)

        if result.returncode == 0:
            print("\nDownload completed successfully!")
        else:
            print(f"\nAn error occurred: {result.stderr}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    download_video(url)
