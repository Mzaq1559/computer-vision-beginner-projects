# Computer Vision Beginner Projects

A collection of small, practical Computer Vision projects built with Python and OpenCV. The goal is to learn Computer Vision fundamentals by implementing concepts from scratch through short, CPU-friendly projects.

> **Learning-focused repository:** each project is intentionally kept simple so the code is easy to read, modify, and experiment with.

## About

Computer Vision can feel overwhelming when starting with topics such as image processing, object detection, tracking, and deep learning. This repository breaks the learning path into small projects that introduce one concept at a time.

The projects start with basic image manipulation and gradually move toward real-time webcam processing and more advanced Computer Vision techniques.

## Projects

| # | Project | Main Concepts | Input |
|---|---|---|---|
| 01 | [Image Basics](01-image-basics) | Reading, resizing, grayscale, cropping, rotation | Image |
| 02 | [Color Detection](02-color-detection) | HSV, masks, thresholding, bitwise operations | Webcam |
| 03 | [Face Detection](03-face-detection) | Haar Cascades, grayscale, bounding boxes | Webcam |
| 04 | [Motion Detection](04-motion-detection) | Frame differences, thresholding, contours | Webcam |
| 05 | Edge Detection | Gaussian blur, Canny, edge maps | Image/Webcam |
| 06 | Shape Detection | Contours, polygon approximation, geometric shapes | Image/Webcam |
| 07 | Document Scanner | Contours, perspective transform, thresholding | Image |
| 08 | Virtual Painter | Color tracking, masks, drawing, coordinates | Webcam |

Projects 05–08 are part of the planned learning path and will be added progressively.

## Learning Path

The recommended order is:

```text
Image Basics
     ↓
Color Detection
     ↓
Face Detection
     ↓
Motion Detection
     ↓
Edge Detection
     ↓
Shape Detection
     ↓
Document Scanner
     ↓
Virtual Painter
```

Each project introduces techniques that are useful in later Computer Vision systems.

## Concepts Covered

### Image Processing

- Reading and writing images
- Image resizing
- Cropping
- Rotation
- Color-space conversion
- Grayscale images
- Gaussian blur
- Thresholding
- Image masks
- Bitwise operations

### Feature and Object Detection

- Edge detection
- Contours
- Bounding boxes
- Polygon approximation
- Haar Cascade face detection
- Basic motion detection

### Real-Time Computer Vision

- Webcam capture with OpenCV
- Frame-by-frame processing
- Real-time visualization
- Keyboard controls
- Simple tracking and drawing

## Tech Stack

- **Python 3**
- **OpenCV**
- **NumPy**

The projects are designed to run on CPU and do not require a dedicated GPU.

## Requirements

- Python 3
- A webcam for projects that use live camera input
- OpenCV
- NumPy

Install the dependencies with:

```bash
pip install -r requirements.txt
```

## Setup

Clone the repository:

```bash
git clone https://github.com/Mzaq1559/computer-vision-beginner-projects.git
cd computer-vision-beginner-projects
```

Create and activate a virtual environment:

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running a Project

Each project is self-contained and has its own README with project-specific instructions.

For example:

```bash
cd 02-color-detection
python main.py
```

Press `q` to quit the webcam-based projects.

## Project Details

### 01 - Image Basics

Introduces the basic operations used to manipulate images with OpenCV.

**What you learn:**

- How OpenCV reads images
- How images are represented as arrays
- Resizing images
- Converting BGR images to grayscale
- Cropping using NumPy slicing
- Rotating images
- Saving processed images

### 02 - Color Detection

Detects a selected color from a webcam stream using HSV color space.

**What you learn:**

- Webcam capture
- BGR vs HSV color spaces
- Defining color ranges
- Creating binary masks
- Bitwise image operations

The example detects green, but the HSV range can be changed to experiment with other colors.

### 03 - Face Detection

Detects faces in a webcam stream using OpenCV's built-in Haar Cascade classifier.

**What you learn:**

- Haar Cascade classifiers
- Grayscale preprocessing
- Object detection
- Bounding boxes
- Detection parameters such as `scaleFactor` and `minNeighbors`

### 04 - Motion Detection

Detects regions of movement by comparing consecutive webcam frames.

**What you learn:**

- Consecutive video frames
- Absolute frame differences
- Thresholding
- Gaussian blur
- Morphological dilation
- Contours
- Bounding boxes

## Repository Structure

```text
computer-vision-beginner-projects/
│
├── 01-image-basics/
│   ├── main.py
│   └── README.md
│
├── 02-color-detection/
│   ├── main.py
│   └── README.md
│
├── 03-face-detection/
│   ├── main.py
│   └── README.md
│
├── 04-motion-detection/
│   ├── main.py
│   └── README.md
│
├── requirements.txt
└── README.md
```

## How to Learn From This Repository

Don't just run the scripts. Try changing them.

For each project:

1. Run the original code.
2. Read the code and identify each OpenCV operation.
3. Change one parameter at a time.
4. Observe how the output changes.
5. Add a small feature of your own.
6. Try rebuilding the project without looking at the original code.

### Suggested Experiments

- Change image dimensions and cropping coordinates.
- Detect a different color.
- Tune HSV thresholds for different lighting conditions.
- Change face detection parameters.
- Change the minimum contour area in motion detection.
- Add FPS information to webcam projects.
- Save webcam output to a video file.
- Add keyboard controls for different modes.

## Why OpenCV?

OpenCV provides the fundamental image-processing and Computer Vision operations needed to understand how many larger systems work. Learning these fundamentals before moving into deep-learning frameworks makes it easier to understand preprocessing, masks, bounding boxes, image transformations, and video pipelines.

## Future Projects

Planned additions include:

- Edge Detection
- Shape Detection
- Document Scanner
- Virtual Painter
- Basic Object Tracking
- Lane Detection
- Color-Based Object Tracking
- Simple Face Recognition
- Background Removal
- Real-Time FPS Monitor

The repository will remain focused on small projects rather than large production applications.

## Who This Is For

This repository is intended for:

- Beginners learning Computer Vision
- Python developers learning OpenCV
- Students building Computer Vision fundamentals
- Anyone who wants small projects for hands-on practice

## Contributing

Suggestions and improvements are welcome.

If you want to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Add or improve a small Computer Vision project.
4. Include a README explaining what the project teaches.
5. Open a pull request.

## Author

**Muhammad Zulqarnain Abdullah**

- GitHub: [@Mzaq1559](https://github.com/Mzaq1559)

## License

This project is intended as an educational learning repository. A formal open-source license can be added when the repository's licensing terms are finalized.
