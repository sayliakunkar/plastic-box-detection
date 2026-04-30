# 🟦 Plastic Box Detection using YOLO

This project uses a custom-trained YOLO model to detect plastic boxes in real-time using a webcam.

---

## 📌 Features

* Real-time object detection using webcam
* Custom YOLO model (`best (2).pt`)
* Adjustable confidence and IoU thresholds
* Simple and lightweight Python implementation

---

## 🛠️ Tech Stack

* Python
* OpenCV (`cv2`)
* Ultralytics YOLO

---

## 📂 Project Structure

```
plasticbox_project/
│── detect_webcam.py
│── best (2).pt
│── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```
git clone https://github.com/sayliakunkar/plastic-box-detection.git
cd plastic-box-detection
```

---

### 2. Install dependencies

```
pip install ultralytics opencv-python
```

---

### 3. Run the script

```
python detect_webcam.py
```

Press **Q** to exit the webcam window.

---

## ⚙️ Configuration

Inside `detect_webcam.py`, you can adjust:

```python
results = model(frame, conf=0.7, iou=0.5)
```

* `conf` → Confidence threshold
* `iou` → Intersection over Union threshold

---

## ⚠️ Important Notes

* Ensure `best (2).pt` is in the same directory as the script
* If the model file is large (>100MB), GitHub may not allow upload
* In that case, use Git LFS or external storage

---

## 🎯 Future Improvements

* Add support for video file input
* Deploy as a web app
* Improve detection accuracy with more training data

---

## 🙌 Author

**Sayli Akunkar**

---

## ⭐ If you like this project

Give it a star on GitHub!
