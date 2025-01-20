import json, cv2, os
from pprint import pprint


path = '/home/vuvanhoc/Documents/build-dataset-for-yolov5/Match_1951_1_0_subclip-20250106T145050Z-001/Match_1951_1_0_subclip/Match_1951_1_0_subclip.json'
data = json.load(open(path))
data = dict(data)
# #dict_keys(['licenses', 'info', 'categories', 'images', 'annotations'])
# # important: categories,
# # data['annotations'][0].keys() : dict_keys(['id', 'image_id', 'category_id', 'segmentation', 'area', 'bbox'])
# # print(data['categories'])
# labesl = ["", "field", "spider", 'ball', 'player']
#
# i = 1
# file_name = data['images'][i]['file_name'][:-3] + "txt"
# #{'id': 2, 'image_id': 1, 'category_id': 1, 'segmentation': [],
# # 'area': 127.9200000000028, 'bbox': [2764.23, 368.04, 7.8, 16.4]} #xc yc, w, h
# category_id = data['annotations'][i]['category_id'] # class_id
# bbox = data['annotations'][i]['bbox'] # bbox
folder_labels_train = './data/train/labels'
folder_labels_val = './data/val/labels'
if not os.path.exists(folder_labels_val):
    os.makedirs(folder_labels_val)
if not os.path.exists(folder_labels_train):
    os.makedirs(folder_labels_train)
# print(bbox)
# img = cv2.imread('/home/vuvanhoc/Documents/build-dataset-for-yolov5/data/train/images/frame_000000.PNG')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# h, w, _ = img.shape
# print(w, h)
# # cv2.imshow('image', img)
# # bbox =
# # for i in range(1300):
# #     file_name = data['images'][i]['file_name'][:-3] + "txt"
# #     with open(f'{folder_labels_train}/{file_name}', 'w') as f:
# #         f.w
# print(labesl[int(category_id)])
# cv2.waitKey(0)
# cv2.destroyAllWindows()
tmp = 0
for id in range(len(data['annotations'])):
    # print(len(data['annotations']))
    image_id = str(data['annotations'][id]['image_id'] - 1) # danh dau frame
    while len(image_id) < 4:
        image_id = "0" + image_id
    # print(('frame thu: ' + image_id)) # ten frame txt
    filename = data['images'][int(image_id)]['file_name'][:-3] + "txt"
    print(filename)
    bbox = data['annotations'][id]['bbox']
    category_id = data['annotations'][id]['category_id']
    # print(category_id, bbox)
    labels = str(
        str(category_id) + " " + str(int(bbox[0])) + " " + str(int(bbox[1])) + " " + str(int(bbox[2])) + " " + str(
            int(bbox[3])) + "\n")
    print(labels)
    if int(image_id) < 1300:
        with open(os.path.join(folder_labels_train, filename), 'a') as f:
            f.write(labels)

    else:
        with open(os.path.join(folder_labels_val, filename), 'a') as f:
            f.write(labels)





