import instaloader

def download_instagram_profile_pictures(username):
    loader = instaloader.Instaloader()
    loader.download_profile(username, profile_pic_only=True)

if __name__ == "__main__":
    username = 'example_user'
    download_instagram_profile_pictures(username)