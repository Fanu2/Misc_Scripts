import instaloader

def download_instagram_image(username, post_shortcode):
    loader = instaloader.Instaloader()
    post = instaloader.Post.from_shortcode(loader.context, post_shortcode)
    loader.download_post(post, target=username)

if __name__ == "__main__":
    username = 'example_user'
    post_shortcode = 'example_shortcode'
    download_instagram_image(username, post_shortcode)