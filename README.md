# Extract MP4 From Folder

A simple Python utility that finds all `.mp4` files inside subfolders and moves them into a single folder.

## Features

- Extracts MP4 files from nested folders
- Supports custom output folder
- Prevents overwriting files with the same name
- Includes dry-run mode to preview changes
- Works from the command line

## Usage

Move all MP4 files into the main folder:

```bash
python extract_mp4.py "C:\Users\YourName\Downloads\Videos"
