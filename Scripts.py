import os

# Define the scripts and their filenames
scripts = {
    'download_youtube_video.py': '''from pytube import YouTube

def download_youtube_video(url, output_path):
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download(output_path)

if __name__ == "__main__":
    url = 'https://www.youtube.com/watch?v=example'
    output_path = 'downloaded_video.mp4'
    download_youtube_video(url, output_path)''',

    'download_youtube_playlist.py': '''from pytube import Playlist

def download_youtube_playlist(url, output_path):
    playlist = Playlist(url)
    for video in playlist.videos:
        video.streams.get_highest_resolution().download(output_path)

if __name__ == "__main__":
    url = 'https://www.youtube.com/playlist?list=example'
    output_path = 'path_to_save_videos'
    download_youtube_playlist(url, output_path)''',

    'download_instagram_image.py': '''import instaloader

def download_instagram_image(username, post_shortcode):
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
    loader.download_post(post, target=username)

if __name__ == "__main__":
    username = 'example_user'
    post_shortcode = 'example_shortcode'
    download_instagram_image(username, post_shortcode)''',

    'download_instagram_profile_pictures.py': '''import instaloader

def download_instagram_profile_pictures(username):
    loader = instaloader.Instaloader()
    loader.download_profile(username, profile_pic_only=True)

if __name__ == "__main__":
    username = 'example_user'
    download_instagram_profile_pictures(username)''',

    'download_twitter_image.py': '''import tweepy
import requests

def download_twitter_image(api_key, api_secret_key, access_token, access_token_secret, tweet_id, output_path):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = api.get_status(tweet_id, tweet_mode='extended')
    media = tweet.entities.get('media', [])
    if len(media) > 0:
        image_url = media[0]['media_url']
        img_data = requests.get(image_url).content
        with open(output_path, 'wb') as handler:
            handler.write(img_data)

if __name__ == "__main__":
    api_key = 'your_api_key'
    api_secret_key = 'your_api_secret_key'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    tweet_id = 'example_tweet_id'
    output_path = 'downloaded_image.jpg'
    download_twitter_image(api_key, api_secret_key, access_token, access_token_secret, tweet_id, output_path)''',

    'download_twitter_video.py': '''import tweepy
from pytube import YouTube

def download_twitter_video(api_key, api_secret_key, access_token, access_token_secret, tweet_id, output_path):
    auth = tweepy.OAuth1UserHandler(api_key, api_secret_key, access_token, access_token_secret)
    api = tweepy.API(auth)
    tweet = api.get_status(tweet_id, tweet_mode='extended')
    media = tweet.extended_entities.get('media', [])
    if len(media) > 0 and media[0]['type'] == 'video':
        video_url = media[0]['video_info']['variants'][0]['url']
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)

if __name__ == "__main__":
    api_key = 'your_api_key'
    api_secret_key = 'your_api_secret_key'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'
    tweet_id = 'example_tweet_id'
    output_path = 'downloaded_video.mp4'
    download_twitter_video(api_key, api_secret_key, access_token, access_token_secret, tweet_id, output_path)''',

    'download_facebook_video.py': '''import os

def download_facebook_video(url, output_path):
    os.system(f'youtube-dl -o {output_path} {url}')

if __name__ == "__main__":
    url = 'https://www.facebook.com/example/video/example'
    output_path = 'downloaded_video.mp4'
    download_facebook_video(url, output_path)''',

    'download_tiktok_video.py': '''import os

def download_tiktok_video(url, output_path):
    os.system(f'youtube-dl -o {output_path} {url}')

if __name__ == "__main__":
    url = 'https://www.tiktok.com/@example/video/example'
    output_path = 'downloaded_video.mp4'
    download_tiktok_video(url, output_path)''',

    'download_soundcloud_track.py': '''import os

def download_soundcloud_track(url, output_path):
    os.system(f'youtube-dl -o {output_path} {url}')

if __name__ == "__main__":
    url = 'https://soundcloud.com/example/track/example'
    output_path = 'downloaded_track.mp3'
    download_soundcloud_track(url, output_path)''',

    'download_reddit_video.py': '''import praw
import os

def download_reddit_video(client_id, client_secret, user_agent, post_url, output_path):
    reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent=user_agent)
    submission = reddit.submission(url=post_url)
    if submission.is_video:
        video_url = submission.media['reddit_video']['fallback_url']
        os.system(f'youtube-dl -o {output_path} {video_url}')

if __name__ == "__main__":
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    user_agent = 'your_user_agent'
    post_url = 'https://www.reddit.com/r/example/comments/example/example/'
    output_path = 'downloaded_video.mp4'
    download_reddit_video(client_id, client_secret, user_agent, post_url, output_path)'''
}

# Path to the project directory
project_dir = '/home/jasvir/PycharmProjects/pythonProject2/'

# Create the files
for filename, content in scripts.items():
    file_path = os.path.join(project_dir, filename)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f"Created: {file_path}")
