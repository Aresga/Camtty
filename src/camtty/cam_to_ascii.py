import argparse
from camtty import CamCharApp

def parse_args():
    parser = argparse.ArgumentParser(description="Display webcam feed as ASCII art in terminal")
    parser.add_argument("--fps", type=int, default=30, help="Target frames per second")
    parser.add_argument("--chars", type=str, default=" .:-=+*#%@", help="ASCII characters to use (from dark to light)")
    parser.add_argument("--camera", type=int, default=0, help="Camera index to use (default: 0)")
    return parser.parse_args()

def main():
    args = parse_args()
    app = CamCharApp(
        camera_index=args.camera,
        ascii_chars=args.chars,
        fps=args.fps
    )
    app.start()

if __name__ == "__main__":
    main()
