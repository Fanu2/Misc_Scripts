from moviepy.editor import VideoFileClip

def create_gif(video_path, output_path, start_time, end_time):
    clip = VideoFileClip(video_path).subclip(start_time, end_time)
    clip.write_gif(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    output_path = 'output.gif'
    start_time = 5  # seconds
    end_time = 10  # seconds
    create_gif(video_path, output_path, start_time, end_time)