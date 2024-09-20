from moviepy.editor import VideoFileClip, CompositeVideoClip

def add_watermark(video_path, watermark_path, output_path, position):
    video = VideoFileClip(video_path)
    watermark = VideoFileClip(watermark_path).resize(height=50)  # Resize watermark if necessary
    watermark = watermark.set_pos(position)
    final = CompositeVideoClip([video, watermark])
    final.write_videofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    watermark_path = 'watermark.png'
    output_path = 'video_with_watermark.mp4'
    add_watermark(video_path, watermark_path, output_path, 'bottom-right')