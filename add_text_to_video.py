from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip

def add_text_to_video(video_path, output_path, text, position, duration):
    video = VideoFileClip(video_path)
    text_clip = TextClip(text, fontsize=70, color='white')
    text_clip = text_clip.set_pos(position).set_duration(duration)
    result = CompositeVideoClip([video, text_clip])
    result.write_videofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    output_path = 'video_with_text.mp4'
    add_text_to_video(video_path, output_path, 'Hello World', 'center', 5)