import tweepy
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
    download_twitter_video(api_key, api_secret_key, access_token, access_token_secret, tweet_id, output_path)