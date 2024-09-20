from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_path):
    video = VideoFileClip(video_path)
    audio = video.audio
    audio.write_audiofile(output_path)

if __name__ == "__main__":
    video_path = 'input_video.mp4'
    output_path = 'extracted_audio.mp3'
    extract_audio(video_path, output_path)