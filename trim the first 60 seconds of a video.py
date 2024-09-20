from moviepy.editor import VideoFileClip

# Path to the video file
video_file = '/home/jasvir/Music/jodha/output_video.mp4'
output_file = '/home/jasvir/Music/jodha/output_video_trimmed.mp4'

# Load the video file
clip = VideoFileClip(video_file)

# Trim the video to the first 60 seconds
trimmed_clip = clip.subclip(0, 60)

# Write the trimmed video to a new file
trimmed_clip.write_videofile(output_file, codec='libx264', audio_codec='aac')
