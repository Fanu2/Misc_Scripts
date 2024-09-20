import tweepy
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
    download_twitter_image(api_key, api_secret_key, access_token, access_token_secret, tweet_id, output_path)