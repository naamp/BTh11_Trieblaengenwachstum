# INFO *Der folgende Code wurde mithilfe von ChatGPT (OpenAI) erstellt und/oder bearbeitet.*

import cv2
import os

# Project name
video_name = "DJI_0674"

# Video path
video_path = f"D:\\BTh11\\20250228_DJIMini3Pro_Video_Ahorn{video_name}.mp4"

# Open video using OpenCV
cam = cv2.VideoCapture(video_path)

# Check if video opened correctly
if not cam.isOpened():
    print("Error: Cannot open video file")
    exit()

# Create output folder if it doesn't exist
output_folder = "data"
os.makedirs(output_folder, exist_ok=True)

# Frame extraction settings
frame_interval = 5  # Every 5th frame
frame_counter = 0
saved_frame_counter = 0

while True:
    # Read the next frame
    ret, frame = cam.read()

    if not ret:
        print("End of video or error reading frames.")
        break  # Exit if video ends or OpenCV fails to read

    # Save every 5th frame
    if frame_counter % frame_interval == 0:
        frame_name = os.path.join(output_folder, f"{video_name}_{frame_counter:06d}.jpg")
        cv2.imwrite(frame_name, frame)
        print(f"Creating... {frame_name}")
        saved_frame_counter += 1

    frame_counter += 1

# Release resources
cam.release()
cv2.destroyAllWindows()

print(f"Finished. Extracted {saved_frame_counter} frames.")
