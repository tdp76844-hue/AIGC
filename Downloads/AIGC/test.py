import cv2
from ultralytics import YOLO

# Tải mô hình YOLOv11
model = YOLO(r"C:\Users\DELL 5490\model.pt")

# Ngưỡng confidence thấp để phát hiện nhiều đối tượng hơn
CONFIDENCE_THRESHOLD = 0.4

def detect_webcam():
    print("\nStarting webcam...")
    print("Press 'q' to quit.\n")
    
    # Mở webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Can't open webcam!")
        return
    
    # Lấy thông tin webcam
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    
    print(f"Info webcam: {width}x{height} @ {fps} FPS")
    print("Start detection...")
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't read from webcam!")
            break
        
        frame_count += 1
        
        # Thực hiện detection
        results = model(frame, conf=CONFIDENCE_THRESHOLD)[0]
        
        # Vẽ kết quả lên frame
        annotated_frame = results.plot()
        
        # Hiển thị frame
        cv2.imshow("YOLOv11 Detection - Webcam", annotated_frame)
        
        # Xử lý phím
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print("Exit...")
            break
    
    # Dọn dẹp
    cap.release()
    cv2.destroyAllWindows()

# Chạy detection với webcam
detect_webcam()
