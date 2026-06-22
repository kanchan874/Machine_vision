# Machine Vision Pre-Lab

A simple Flask web application built for a Machine Vision pre-lab practical.
It demonstrates core OpenCV/NumPy concepts through a browser-based UI:

- Image loading (upload / demo image)
- Image display
- Image properties (width, height, channels, dtype, memory size, total pixels)
- Color channel splitting (R, G, B) and color-space conversion (Grayscale, HSV)
- Video capture and webcam access (start/stop, live feed, snapshot)

## Folder Structure

```
MachineVision/
│
├── app.py                 # Flask backend (OpenCV + NumPy logic)
├── requirements.txt       # Python dependencies
├── README.md
├── templates/
│   └── index.html         # Frontend (HTML/CSS/JS)
└── static/
    ├── uploads/           # Uploaded / demo / snapshot images (auto-created)
    └── outputs/           # Generated channel/grayscale/HSV images (auto-created)
```

## Requirements

- Python 3.8+
- A webcam (for the Webcam section — optional, the rest of the app works without it)
- Recommended editor: VS Code or Jupyter Notebook (for exploring OpenCV separately)

## Installation

1. **Clone or download** this folder.

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```
   Activate it:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   - `Flask` – web server
   - `opencv-python` – image/video processing
   - `numpy` – array operations
   - `matplotlib` – included per practical requirement (image backend utility)

## Running the App

```bash
python app.py
```

Then open your browser at:

```
http://127.0.0.1:5000/
```

## How to Use

1. **Load Image** tab
   - Click **Upload Image** to choose a picture from your computer, or
   - Click **Load Demo Image** to generate and load a sample image (no file needed).

2. **Image Properties** tab
   - Click **Show Properties** to view width, height, channels, data type,
     total pixels, and memory size of the currently loaded image
     (uses `img.shape`, `img.dtype`, `img.nbytes`).

3. **Color Channels** tab
   - Click **Generate Channels** to view the original image alongside its
     Red, Green, Blue channels (`cv2.split()`), Grayscale, and HSV versions
     (`cv2.cvtColor()`).

4. **Webcam** tab
   - Click **Start Webcam** to begin a live feed from your camera
     (`cv2.VideoCapture(0)`).
   - Click **Capture Snapshot** to save the current frame as an image.
   - Click **Stop Webcam** to release the camera.

## Notes

- The app uses a single shared "current image" to keep the demo simple,
  which is suitable for one user testing on localhost. Refreshing the page
  does not affect the loaded image — only uploading a new one, loading the
  demo image, or taking a snapshot updates it.
- If the webcam does not start, make sure no other application is using it
  and that your browser/OS has granted camera permission to Python.
- Generated files are saved under `static/uploads/` and `static/outputs/`
  and are recreated automatically each time the app runs.

## Tech Stack

| Layer    | Technology                  |
|----------|------------------------------|
| Backend  | Python, Flask, OpenCV, NumPy |
| Frontend | HTML, CSS, JavaScript        |
| Extra    | Matplotlib (per practical requirement) |