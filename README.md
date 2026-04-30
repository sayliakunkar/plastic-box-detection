# 🟦 Plastic Box Detection using YOLO

This project uses a custom-trained YOLO model to detect plastic boxes in real-time using a webcam.

---

## 📌 Features

* Real-time object detection using webcam
* Custom-trained YOLO model
* Adjustable confidence and IoU thresholds
* Simple and easy-to-run Python script

---

## 🛠️ Tech Stack

* Python
* OpenCV (`cv2`)
* Ultralytics YOLO

---

## 📂 Project Structure

```id="e1x3k9"
plasticbox_project/
│── detect_webcam.py
│── best (2).pt
│── dataset/
│   ├── images/
│   ├── labels/
│   ├── data.yaml
│── output.png
│── README.md
```

---

## ▶️ How to Run

### 1. Clone the repository

```id="u5yx3g"
git clone https://github.com/sayliakunkar/plastic-box-detection.git
cd plastic-box-detection
```

---

### 2. Install dependencies

```id="r3v2y8"
pip install ultralytics opencv-python
```

---

### 3. Run the project

```id="q4z8kp"
python detect_webcam.py
```

Press **Q** to exit the webcam window.

---

## ⚙️ Configuration

You can adjust detection settings in `detect_webcam.py`:

```python id="p9k2jd"
results = model(frame, conf=0.7, iou=0.5)
```

* `conf` → Confidence threshold
* `iou` → Intersection over Union threshold

---

## 📊 Dataset

This project uses a custom-labeled dataset for plastic box detection.

### 📂 Structure

```id="s2k8dh"
dataset/
│── images/
│── labels/
│── data.yaml
```

### 🏷️ Label Format (YOLO)

Each label file contains:

```id="m8x1qp"
class_id x_center y_center width height
```

### 📌 Classes

* 0 → Plastic Box

---

## 📸 Output

Example detection result:

```id="f8k3lp"
![Detection Output](output.png)
```

---

## ⚠️ Important Notes

* Ensure `best (2).pt` is in the same directory as the script
* If dataset or model is large (>100MB), use Git LFS or external storage
* Update file paths if running on a different system

---

## 🎯 Future Improvements

* Add video file detection
* Deploy as a web application
* Improve model accuracy with more data

---

## 🙌 Author

**Sayli Akunkar**

---

## ⭐ Support

If you like this project, consider giving it a star ⭐ on GitHub!
