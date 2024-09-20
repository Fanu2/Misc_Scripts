from moviepy.editor import VideoFileClip

def crop_video(video_path, output_path, x1, y1, x2, y2):
    video = VideoFileClip(video_path)
    cropped_video = video.crop(x1=x1, y1=y1, x2=x2, y2=y2)
    cropped_video.write_videofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    output_path = 'cropped_video.mp4'
    crop_video(video_path, output_path, 100, 50, 500, 400)