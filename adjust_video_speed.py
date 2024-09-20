from moviepy.editor import VideoFileClip

def adjust_video_speed(video_path, output_path, speed_factor):
    video = VideoFileClip(video_path)
    adjusted_video = video.fx(vfx.speedx, speed_factor)
    adjusted_video.write_videofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    output_path = 'adjusted_speed_video.mp4'
    speed_factor = 2  # 2x speed
    adjust_video_speed(video_path, output_path, speed_factor)