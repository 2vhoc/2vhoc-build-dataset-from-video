# Video Dataset Creation / Tạo Dataset từ Video

[English](#english) | [Tiếng Việt](#tiếng-việt)

## English

### Introduction
This repository contains tools and scripts for creating annotated datasets from video sources. It helps you extract frames from videos and create corresponding annotations for computer vision tasks.

### Demo
![Visualization Example](https://github.com/2vhoc/build-dataset-from-video/raw/main/Match_1951_1_0_subclip-20250106T145050Z-001/Chụp%20màn%20hình%20từ%202025-01-20%2016-20-28.png)
*Example of object detection visualization with bounding boxes*

### Features
- Extract frames from video at specified intervals
- Use as training data for YOLOv5 models

### Installation
```bash
git clone https://github.com/2vhoc/2vhoc-build-dataset-from-video
pip install -r requirements.txt
```

### Usage
1. **Frame Extraction**
   ```python
   python video_to_frame.py
   ```

2. **Extract labels and bounding boxes**
   ```python
   python extract_labels.py
   ```

3. **Visualization**
   ```python
   python visualize.py --image 1000
   ```

### Directory Structure
```
video-dataset-tools/
├── data/
│   ├── tags.json
│   ├── train # run code to create folder
│   │   ├── images
│   │   └── labels
│   ├── val # run code to create folder
│       ├── images
│       └── labels
│
├── extract_labels.py
├── requirements.txt  
├── video_to_frame.py   
├── visualize.py
│   
└── Match_1951_1_0_subclip-20250106T145050Z-001/
    └── Match_1951_1_0_subclip/
        ├── Match_1951_1_0_subclip.mp4
        └── Match_1951_1_0_subclip.json
```

### System Requirements
- Python 3.8+
- OpenCV

---

## Tiếng Việt

### Giới thiệu
Repository này chứa các công cụ và script để tạo bộ dữ liệu có chú thích từ nguồn video. Nó giúp bạn trích xuất các khung hình từ video và tạo các chú thích tương ứng cho các tác vụ thị giác máy tính.

### Demo
![Ví dụ trực quan hóa](https://github.com/2vhoc/build-dataset-from-video/raw/main/Match_1951_1_0_subclip-20250106T145050Z-001/Chụp%20màn%20hình%20từ%202025-01-20%2016-20-28.png)
*Ví dụ về trực quan hóa phát hiện đối tượng với bounding box*


### Tính năng
- Trích xuất khung hình từ video theo khoảng thời gian xác định
- Dùng làm data cho mô hình yolov5

### Cài đặt
```bash
git clone https://github.com/2vhoc/2vhoc-build-dataset-from-video
pip install -r requirements.txt
```

### Sử dụng
1. **Trích xuất khung hình**
   ```python
   python video_to_frame.py 
   ```

2. **Trích xuất labels, bbox**
   ```python
   python extract_labels.py
   ```

3. **Trực quan hoá**
   ```python
   python visualize.py --image 1000 
   ```

### Cấu trúc thư mục
```
video-dataset-tools/
├── data/
│   ├── tags.json
│   ├── train # run code to create folder
│   │   ├── images
│   │   └── labels
│   ├── val # run code to create folder
│       ├── images
│       └── labels
│
├── extract_labels.py
├── requirements.txt  
├── video_to_frame.py   
├── visualize.py
│   
└── Match_1951_1_0_subclip-20250106T145050Z-001/
    └── Match_1951_1_0_subclip/
        ├── Match_1951_1_0_subclip.mp4
        └── Match_1951_1_0_subclip.json
```

### Yêu cầu hệ thống
- Python 3.8+
- OpenCV
