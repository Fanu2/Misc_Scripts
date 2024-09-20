from moviepy.editor import VideoFileClip, AudioFileClip

def add_background_music(video_path, audio_path, output_path):
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path).subclip(0, video.duration)
    video = video.set_audio(audio)
    video.write_videofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    audio_path = 'background_music.mp3'
    output_path = 'video_with_music.mp4'
    add_background_music(video_path, audio_path, output_path)