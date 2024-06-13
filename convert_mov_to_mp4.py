import os
import subprocess
import sys

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("ffmpeg is installed and available.")
    except subprocess.CalledProcessError:
        print("ffmpeg is not installed or not found in PATH.")
        sys.exit(1)

def convert_mov_to_mp4(input_file):
    if not input_file.endswith(".mov"):
        print("The specified file is not a .mov file.")
        return

    output_file = os.path.splitext(input_file)[0] + ".mp4"
    
    command = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", "h264",
        "-acodec", "aac",
        output_file
    ]
    
    try:
        subprocess.run(command, check=True)
        print(f"Successfully converted {input_file} to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {input_file}: {e}")

if __name__ == "__main__":
    check_ffmpeg()
    if len(sys.argv) != 2:
        print("Usage: python convert_mov_to_mp4.py <path_to_mov_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    if not os.path.isfile(input_file):
        print(f"The file {input_file} does not exist.")
        sys.exit(1)

    convert_mov_to_mp4(input_file)