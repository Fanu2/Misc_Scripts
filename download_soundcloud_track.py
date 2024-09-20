import os

def download_soundcloud_track(url, output_path):
    os.system(f'youtube-dl -o {output_path} {url}')

if __name__ == "__main__":
    url = 'https://soundcloud.com/example/track/example'
    output_path = 'downloaded_track.mp3'
    download_soundcloud_track(url, output_path)