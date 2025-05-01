import numpy as np
import cv2

class ASCIIConverter:
    def __init__(self, chars=" .:-=+*#%@"):
        self.ascii_chars = chars
        self._generate_ascii_map()

    def _generate_ascii_map(self):
        """Precompute ASCII mappings for better performance"""
        self.ascii_map = [self.ascii_chars[int(i / 256 * len(self.ascii_chars))] 
                         for i in range(256)]

    def pixel_to_ascii(self, pixel):
        """Convert a single pixel value to ASCII character"""
        return self.ascii_map[pixel]

    def frame_to_ascii(self, frame, width, height):
        """Convert an entire frame to ASCII art"""
        # Resize frame to fit desired dimensions
        resized = cv2.resize(frame, (width, height))
        # Convert to grayscale
        gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
        # Convert to ASCII
        ascii_img = ["".join([self.pixel_to_ascii(pixel) for pixel in row]) 
                    for row in gray]
        return "\n".join(ascii_img)