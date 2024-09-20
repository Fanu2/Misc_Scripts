from pytube import Playlist

def download_youtube_playlist(url, output_path):
    playlist = Playlist(url)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path)

if __name__ == "__main__":
    url = 'https://www.youtube.com/playlist?list=example'
    output_path = 'path_to_save_videos'
    download_youtube_playlist(url, output_path)