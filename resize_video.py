from moviepy.editor import VideoFileClip

def resize_video(video_path, output_path, width):
    video = VideoFileClip(video_path)
    resized_video = video.resize(width=width)
    resized_video.write_videofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    output_path = 'resized_video.mp4'
    width = 640  # pixels
    resize_video(video_path, output_path, width)