from pytube import YouTube

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=example'
    output_path = 'downloaded_video.mp4'
    download_youtube_video(url, output_path)