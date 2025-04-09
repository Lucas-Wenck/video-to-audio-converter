import subprocess
import os
from sys import platform

def convert_video_to_audio(video_file, output_ext="wav"):
    filename, ext = os.path.splitext(video_file)
    if platform == "win32":
        subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], shell=True)
    else:
        subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"])
