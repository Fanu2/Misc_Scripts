from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(video_paths, output_path):
    clips = [VideoFileClip(video) for video in video_paths]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_path)

if __name__ == "__main__":
    video_paths = ['video1.mp4', 'video2.mp4', 'video3.mp4']
    output_path = 'concatenated_video.mp4'
    concatenate_videos(video_paths, output_path)