from moviepy.editor import *
from moviepy.video.fx.all import fadein, fadeout

# File paths
image1_path = "/home/jasvir/Music/jodha/1.jpg"
image2_path = "/home/jasvir/Music/jodha/2.jpg"
audio_path = "/home/jasvir/Music/jodha/Woh Jab Yaad Aaye.m4a"
output_path = "/home/jasvir/Music/jodha/jodha.mp4"

# Load images and audio
image1 = ImageClip(image1_path)
image2 = ImageClip(image2_path)
audio = AudioFileClip(audio_path)

# Set the duration of each image clip to match half the length of the audio
audio_duration = audio.duration
image_duration = audio_duration / 2

# Resize images to fit the screen and set duration
image1 = image1.set_duration(image_duration).resize(height=720)
image2 = image2.set_duration(image_duration).resize(height=720)

# Apply effects to images
image1 = fadein(image1, duration=1).fadeout(duration=1)
image2 = fadein(image2, duration=1).fadeout(duration=1)

# Crossfade between images
video = concatenate_videoclips([image1.crossfadein(1), image2.crossfadein(1)], method="compose")

# Set the audio to the video
video = video.set_audio(audio)

# Set the final duration to match the audio length
video = video.set_duration(audio_duration)

# Write the final video file
video.write_videofile(output_path, fps=24, codec='libx264')
