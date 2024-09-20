from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips
import os
import random

# Paths
image_folder = '/home/jasvir/Music/jodha/'
audio_file = os.path.join(image_folder, 'dhuri.m4a')
output_file = '/home/jasvir/Music/jodha/output_video.mp4'

# Get image files
image_files = [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('png', 'jpg', 'jpeg'))]
if not image_files:
    raise ValueError("No images found in the specified folder.")

# Shuffle images
random.shuffle(image_files)

# Create video clips from images with slide effect
clips = []
image_duration = 2  # Duration of each image in seconds
for img in image_files:
    clip = ImageSequenceClip([img], fps=24)  # Create clip with 24 fps
    clip = clip.set_duration(image_duration)  # Set duration for each image
    clips.append(clip)

# Concatenate clips with slide effect
final_clip = concatenate_videoclips(clips, method="compose")

# Set audio
audio = AudioFileClip(audio_file)
final_clip = final_clip.set_audio(audio)

# Make video duration equal to audio duration
final_clip = final_clip.subclip(0, audio.duration)

# Write the result to a file
final_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
