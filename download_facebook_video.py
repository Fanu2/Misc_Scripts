import os

def download_facebook_video(url, output_path):
    os.system(f'youtube-dl -o {output_path} {url}')

if __name__ == "__main__":
    url = 'https://www.facebook.com/example/video/example'
    output_path = 'downloaded_video.mp4'
    download_facebook_video(url, output_path)