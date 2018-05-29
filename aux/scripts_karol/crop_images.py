import json
import cv2


counter = 0

result_json = []

with open("../data/oidv3.json") as f:
    data = json.load(f)

for key in sorted(data.keys()):
    img = cv2.imread("../../images/"+key)
    for bbox in data[key]:
        box = {'orig_fname': key, "fname": "img%08d.jpg" % counter,
               "class": bbox['name']}
        xmin = int(img.shape[1] * float(bbox['ymin']))
        ymin = int(img.shape[0] * float(bbox['xmin']))
        xmax = int(img.shape[1] * float(bbox['ymax']))
        ymax = int(img.shape[0] * float(bbox['xmax']))
        cropped = img[ymin:ymax, xmin:xmax, :]
        cv2.imwrite("cropped_images/img%08d.jpg" % counter, cropped)
        counter = counter + 1
        result_json.append(box)

with open('../data/cropped_oidv3.json', 'w') as f:
    json.dump(result_json, f)
