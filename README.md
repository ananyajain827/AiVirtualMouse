# 🖱️ AI Virtual Mouse using OpenCV & MediaPipe

An AI-powered virtual mouse that lets users control their computer cursor using **hand gestures** detected by a webcam.  
This project uses **MediaPipe**, **OpenCV**, and **PyAutoGUI** to simulate real-time mouse movement and clicking — all without a physical mouse! 🧠🖐️💻

---

## 📌 Table of Contents

- [📌 Features](#-features)
- [🎥 Demo](#-demo)
- [🛠 Technologies Used](#-technologies-used)
- [🚀 Getting Started](#-getting-started)
- [⚙️ How It Works](#️-how-it-works)
- [📦 Possible Enhancements](#-possible-enhancements)
- [🙋 Author](#-author)
- [📄 License](#-license)

---

## ✨ Features

- 🎯 Cursor movement via index finger tracking
- 👌 Click detection by touching index finger and thumb
- 🔁 Smooth motion using recent position averaging
- 🧩 Modular structure — easy to add more gestures (drag, right-click, etc.)
- 📐 Maps camera frame coordinates to screen resolution accurately

---

## 🎥 Demo



---

## 🛠 Technologies Used

| Library       | Purpose                                |
|---------------|----------------------------------------|
| `OpenCV`      | Webcam capture and frame processing    |
| `MediaPipe`   | Real-time hand detection and tracking  |
| `PyAutoGUI`   | Cursor movement and click simulation   |
| `NumPy`       | Coordinate mapping and smoothing       |
| `Python`      | Primary language for development       |

---

## 🚀 Getting Started

### 📁 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-virtual-mouse.git
cd ai-virtual-mouse
```

###📦 2. Install Required Libraries
```bash
pip install opencv-python mediapipe pyautogui numpy
```

### ▶️ 3. Run the Program
```bash
python virtual_mouse.py
```

---

### ⚙️ How It Works
🎥 Captures video feed from your webcam

✋ Detects your hand using MediaPipe's hand landmarks

🧠 Tracks the index finger (landmark 8) to control the mouse cursor

👌 Checks the distance between index finger and thumb (landmark 4) to trigger a click

🔁 Smoothens cursor movement using recent positions

🖱️ Maps hand position in the camera frame to actual screen coordinates using PyAutoGUI

---

## 📦 Possible Enhancements
✌️ Right-click gesture using middle finger

🖱️ Drag and drop feature with hold gesture

🔄 Scroll gesture using two fingers

🎛 GUI overlay for calibration and feedback

🌐 Multi-screen support

---

## 🙋 Author
Ananya
👩‍🎓 B.Tech Computer Science | 💻 Developer 
🔗 [LinkedIn](https://www.linkedin.com/in/ananya-jain-01104427b/) • 🌐 Portfolio

If you like this project, don't forget to ⭐ the repository and share it!

---

## 📄 License
This project is licensed under the MIT License.
See the LICENSE file for more details.
