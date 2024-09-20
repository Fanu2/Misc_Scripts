from moviepy.editor import ImageSequenceClip

def create_slideshow(image_paths, output_path, fps):
    clip = ImageSequenceClip(image_paths, fps=fps)
    clip.write_videofile(output_path)

if __name__ == "__main__":
    image_paths = ['image1.jpg', 'image2.jpg', 'image3.jpg']
    output_path = 'slideshow.mp4'
    fps = 1  # frames per second
    create_slideshow(image_paths, output_path, fps)