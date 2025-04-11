import os
from tkinter import filedialog
import subprocess
from sys import platform

def browse_file(choice: str):

    if choice == "Video to Audio" or choice == "Video to Video":
        filetypes = (("Video files", "*.mp4 *.avi *.mov *.mkv *.flv *.wmv"), ("All files", "*.*"))
    elif choice == "Audio to Audio":
        filetypes = (("Audio files", "*.mp3 *.aac *.wav *.flac"), ("All files", "*.*"))

    file_path = filedialog.askopenfilename(
        title="Select video file",
        initialdir=os.path.expanduser("~"),
        filetypes=filetypes
    )

    if file_path:
        return file_path
    
    return None

def convert_video_to_audio(video_file, output_ext="wav"):
    filename, ext = os.path.splitext(video_file)
    if platform == "win32":
        subprocess.run(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], shell=True)
    else:
        subprocess.Popen(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"])
