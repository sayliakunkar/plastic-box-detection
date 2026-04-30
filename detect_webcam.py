from ultralytics import YOLO
import cv2

model = YOLO(r'C:\Users\Hp\OneDrive\Desktop\plasticbox_project\best (2).pt')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.7, iou=0.5)
    annotated = results[0].plot()

    cv2.imshow('Plastic Box Detection', annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()