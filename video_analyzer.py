import cv2
import os
import json


def analyze_video(file_path):
    if not os.path.exists(file_path):
        print("Error: Video file does not exist.")
        return

    # File information
    file_name = os.path.basename(file_path)
    file_size = os.path.getsize(file_path)

    # Open video
    video = cv2.VideoCapture(file_path)

    if not video.isOpened():
        print("Error: Could not open video.")
        return

    # Video properties
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # Duration
    duration = frame_count / fps if fps > 0 else 0

    # Codec
    codec = int(video.get(cv2.CAP_PROP_FOURCC))
    codec_name = "".join([
        chr(codec & 0xFF),
        chr((codec >> 8) & 0xFF),
        chr((codec >> 16) & 0xFF),
        chr((codec >> 24) & 0xFF)
    ])

    video.release()

    # Convert file size
    file_size_mb = file_size / (1024 * 1024)

    # Prepare report
    report = {
        "file_name": file_name,
        "file_size": f"{file_size_mb:.2f} MB",
        "container": os.path.splitext(file_path)[1].replace(".", "").upper(),
        "duration": f"{duration:.2f} seconds",
        "video": {
            "resolution": f"{width} x {height}",
            "frame_rate": f"{fps:.2f} FPS",
            "frame_count": frame_count,
            "codec": codec_name.strip() or "Unknown"
        }
    }

    # Display report
    print("\n================================")
    print("       VIDEO METADATA REPORT")
    print("================================")

    print(f"\nFile Name       : {report['file_name']}")
    print(f"File Size       : {report['file_size']}")
    print(f"Container       : {report['container']}")
    print(f"Duration        : {report['duration']}")

    print("\nVIDEO")
    print("--------------------------------")
    print(f"Resolution      : {report['video']['resolution']}")
    print(f"Frame Rate      : {report['video']['frame_rate']}")
    print(f"Frame Count     : {report['video']['frame_count']}")
    print(f"Codec           : {report['video']['codec']}")

    print("\nAUDIO")
    print("--------------------------------")
    print("Codec           : Not available with OpenCV")
    print("Channels        : Not available with OpenCV")
    print("Sampling Rate   : Not available with OpenCV")
    print("Bit Rate        : Not available with OpenCV")

    return report
video_path = r"C:\Users\hp\Downloads\1zy-gy94fp.mp4"

if __name__ == "__main__":
    video_path = "samples/video.mp4"

    result = analyze_video(video_path)