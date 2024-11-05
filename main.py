import subprocess
import os
import sys

def convert_video_to_audio(video_file, output_ext="mp3"):
    filename, ext = os.path.splitext(video_file)
    subprocess.call(["ffmpeg", "-y", "-i", video_file, f"{filename}.{output_ext}"], stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)

def dir_loop(source):
    for file in os.listdir(source):
        if file == "main.py":
            continue
        convert_video_to_audio(f"{source}{file}")
        os.remove(f"{source}{file}")

if __name__ == "__main__":
    vf = sys.argv[1]
    dir_loop(vf)