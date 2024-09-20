from moviepy.editor import (ImageClip, VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeVideoClip, ColorClip)
from moviepy.video.fx import fadein, fadeout
from moviepy.video.fx.all import colorx
import numpy as np

# Paths
image1_path = '/home/jasvir/Music/jodha/1.png'
image2_path = '/home/jasvir/Music/jodha/2.png'
audio_path = '/home/jasvir/Music/jodha/1.m4a'
output_file = '/home/jasvir/Music/jodha/output_video_with_gradient.mp4'

# Parameters
video_duration = 60  # Duration of the video in seconds
image_size = (1920, 1080)  # Size of the video frame

# Load images and create image clips
image1 = ImageClip(image1_path).resize(image_size).set_duration(video_duration)
image2 = ImageClip(image2_path).resize(image_size).set_duration(video_duration)

# Create gradient overlay for the first image
def create_gradient(size):
    """Create a vertical gradient image."""
    gradient = np.zeros((size[1], size[0], 3), dtype=np.uint8)
    for y in range(size[1]):
        gradient[y, :, :] = [0, 0, int(255 * (y / size[1]))]  # Change color from black to blue gradient
    return gradient

gradient_image = create_gradient(image_size)
gradient_clip = ImageClip(gradient_image, ismask=False).set_duration(video_duration).resize(image_size)

# Combine gradient with the first image
layer1_with_gradient = CompositeVideoClip([image1.set_opacity(0.5), gradient_clip])

# Create the final video clip by layering images
final_clip = CompositeVideoClip([layer1_with_gradient, image2])

# Load audio and set it to the video
audio = AudioFileClip(audio_path).subclip(0, video_duration)
final_clip = final_clip.set_audio(audio)

# Write the result to a file
final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac', fps=24)
