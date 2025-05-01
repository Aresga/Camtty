import cv2
import numpy as np
import os
import sys
import time

# ASCII characters from dark to light
ASCII_CHARS = " .:-=+*#%@"

# Get terminal size
TERMINAL_WIDTH = os.get_terminal_size().columns
TERMINAL_HEIGHT = os.get_terminal_size().lines - 2  #space for a prompt

# Map a pixel value (0-255) to an ASCII char
def pixel_to_ascii(pixel):
    return ASCII_CHARS[int(pixel / 256 * len(ASCII_CHARS))]

def frame_to_ascii(frame, width, height):
    # Resize frame to fit terminal
    frame = cv2.resize(frame, (width, height))
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Map pixels to ASCII
    ascii_img = ["".join([pixel_to_ascii(pixel) for pixel in row]) for row in gray]
    return "\n".join(ascii_img)

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Could not open webcam.")
        sys.exit(1)
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            ascii_frame = frame_to_ascii(frame, TERMINAL_WIDTH, TERMINAL_HEIGHT)
            print("\033[H\033[J", end="")  #RESET 
            print(ascii_frame)
            time.sleep(0.033)  # ~30 FPS
    except KeyboardInterrupt:
        pass
    finally:
        cap.release()
        print("\nExiting...")

if __name__ == "__main__":
    main()
