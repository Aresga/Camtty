from .ascii_converter import ASCIIConverter
from .camera_handler import CameraHandler
from .terminal_display import TerminalDisplay
import sys

class CamCharApp:
    def __init__(self, camera_index=0, ascii_chars=" .:-=+*#%@", fps=30):
        self.converter = ASCIIConverter(ascii_chars)
        self.camera = CameraHandler(camera_index)
        self.display = TerminalDisplay()
        self.display.set_fps(fps)
        self.running = False

    def start(self):
        """Start the ASCII webcam feed"""
        try:
            self.running = True
            self.camera.start()
            
            while self.running:
                # Get terminal dimensions
                width, height = self.display.get_terminal_size()
                if width < 10 or height < 5:
                    print("Terminal size too small")
                    break

                # Capture and convert frame
                frame = self.camera.get_frame()
                if frame is None:
                    break
                
                # Convert to ASCII and display
                ascii_frame = self.converter.frame_to_ascii(frame, width, height)
                self.display.display_frame(ascii_frame)

        except KeyboardInterrupt:
            pass
        finally:
            self.stop()

    def stop(self):
        """Stop the application and clean up resources"""
        self.running = False
        self.camera.release()