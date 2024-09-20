import praw
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
    download_reddit_video(client_id, client_secret, user_agent, post_url, output_path)