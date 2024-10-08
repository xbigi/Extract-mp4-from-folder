import shutil
import os

def extract_mp4_videos(main_folder):
 

  for root, dirs, files in os.walk(main_folder):
    for file in files:
      if file.endswith(".mp4"):
        shutil.move(os.path.join(root, file), main_folder)

if __name__ == "__main__":
  main_folder = "REPLACE THIS"
  extract_mp4_videos(main_folder)