import os, cv2


folder_images_train = './data/train/images'
folder_labels_train = './data/train/labels'
folder_images_val = './data/val/images'
folder_labels_val = './data/val/labels'
if not os.path.exists(folder_images_train):
    os.makedirs(folder_images_train)

if not os.path.exists(folder_labels_train):
    os.makedirs(folder_labels_train)

if not os.path.exists(folder_images_val):
    os.makedirs(folder_images_val)

if not os.path.exists(folder_labels_val):
    os.makedirs(folder_labels_val)

cap = cv2.VideoCapture('/home/vuvanhoc/Documents/build-dataset-for-yolov5/Match_1951_1_0_subclip-20250106T145050Z-001/Match_1951_1_0_subclip/Match_1951_1_0_subclip.mp4')

i = 0
while(cap.isOpened()):
    tmp = str(i)
    ret, frame = cap.read()
    while len(tmp) < 4:
        tmp = "0" + tmp
    if not ret:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    if i <= 1299:
        cv2.imwrite(f'{folder_images_train}/frame_00{tmp}.PNG', frame)
    else: cv2.imwrite(f'{folder_images_val}/frame_00{tmp}.PNG', frame)
    i += 1
