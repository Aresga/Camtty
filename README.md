# Camtty 📸 -> 💻 -> 🎨

**Turn your webcam feed into live ASCII art directly in your terminal!**

Camtty is a fun command-line tool that captures video from your webcam, converts each frame into ASCII characters, and displays the result in real-time in your terminal.



## ✨ Features

*   **Live Webcam Feed:** See the world around you rendered in ASCII.
*   **Real-time Conversion:** Fast conversion process for a smooth experience.
*   **Terminal-Based:** Runs entirely within your terminal using libraries like `blessed`.

## 🚀 Installation

1.  **Prerequisites:**
    *   Python 3.7+
    *   `pip` (Python package installer)
    *   A connected webcam recognized by your system.

2.  **Install using pip:**
    ```bash
    pip install camtty
    ```
    *Alternatively, for local development:*
    ```bash
    # Clone the repository (if you haven't already)
    # git clone <your-repo-url>
    # cd camchar
    pip install .
    ```

## 🎮 Usage

Simply run the following command in your terminal:

```bash
camtty
```

Press `Ctrl+C` or `q` to stop the stream.



## 🔧 How it Works

Camtty uses:

*   **OpenCV (`opencv-python`)**: To capture video frames from the webcam.
*   **NumPy**: For efficient numerical operations on image data.
*   **Blessed**: To control the terminal and display the ASCII art smoothly.

The core logic involves:
1.  Capturing a frame from the webcam.
2.  Resizing the frame (optional, for performance/fit).
3.  Converting the frame to grayscale.
4.  Mapping pixel intensity values to ASCII characters.
5.  Printing the resulting ASCII string to the terminal using `blessed` for positioning.

## 🤝 Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the [LICENSE_NAME] License - see the [LICENSE](LICENSE) file for details.

---


