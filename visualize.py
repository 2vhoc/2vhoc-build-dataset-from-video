import cv2, os, json, argparse
tags = json.load(open('/home/vuvanhoc/Documents/build-dataset-for-yolov5/data/tags.json'))

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image',type=str ,default="0", help='Number of images')
    return parser.parse_args()


number = args().image
while len(number) < 4:
    number ="0" + number
img = cv2.imread(f'/home/vuvanhoc/Documents/build-dataset-for-yolov5/data/train/images/frame_00{number}.PNG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
labels = []
tags = tags['tags']
with open(f'/home/vuvanhoc/Documents/build-dataset-for-yolov5/data/train/labels/frame_00{number}.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip().split(' ')
        tag = int(line[0])
        xmin = int(line[1])
        ymin = int(line[2])
        w = int(line[3])
        h = int(line[4])
        cv2.putText(img, tags[tag], (xmin, ymin-10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        cv2.rectangle(img, (xmin, ymin), (xmin + w, ymin + h), (255, 0, 0), 2)


cv2.imshow('frame', img)


#
cv2.waitKey(0)
cv2.destroyAllWindows()