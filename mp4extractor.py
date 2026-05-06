import argparse
import shutil
from pathlib import Path


def get_unique_path(destination: Path) -> Path:
    if not destination.exists():
        return destination

    counter = 1
    stem = destination.stem
    suffix = destination.suffix

    while True:
        new_path = destination.with_name(f"{stem}_{counter}{suffix}")
        if not new_path.exists():
            return new_path
        counter += 1


def extract_mp4_videos(source_folder: Path, output_folder: Path, dry_run: bool = False) -> int:
    moved_count = 0

    for file_path in source_folder.rglob("*.mp4"):
        if file_path.parent == output_folder:
            continue

        destination = get_unique_path(output_folder / file_path.name)

        if dry_run:
            print(f"[DRY RUN] {file_path} -> {destination}")
        else:
            shutil.move(str(file_path), str(destination))
            print(f"Moved: {file_path.name}")

        moved_count += 1

    return moved_count


def main():
    parser = argparse.ArgumentParser(
        description="Extract all MP4 files from subfolders into one folder."
    )

    parser.add_argument(
        "source",
        help="Main folder containing subfolders with MP4 files"
    )

    parser.add_argument(
        "-o",
        "--output",
        help="Destination folder. Default: same as source folder",
        default=None
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview files without moving them"
    )

    args = parser.parse_args()

    source_folder = Path(args.source).expanduser().resolve()
    output_folder = Path(args.output).expanduser().resolve() if args.output else source_folder

    if not source_folder.exists():
        print("Error: source folder does not exist.")
        return

    output_folder.mkdir(parents=True, exist_ok=True)

    total = extract_mp4_videos(source_folder, output_folder, args.dry_run)

    print(f"\nDone. {total} MP4 file(s) found.")


if __name__ == "__main__":
    main()
