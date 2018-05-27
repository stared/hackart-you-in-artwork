import json
# import cv2

counter = 0

result_json = []

with open("../data/oidv3.json") as f:
    data_oid = json.load(f)
# for key in sorted(data.keys()):
#     img = cv2.imread("../../images/"+key)
#     # img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
#     # cv2.imshow('img', img)
#     for bbox in data[key]:
#         box = {'orig_fname': key, "fname": "img%08d.jpg" % counter,
#                "class": bbox['name']}
#         xmin = int(img.shape[1] * float(bbox['ymin']))
#         ymin = int(img.shape[0] * float(bbox['xmin']))
#         xmax = int(img.shape[1] * float(bbox['ymax']))
#         ymax = int(img.shape[0] * float(bbox['xmax']))
#         cropped = img[ymin:ymax, xmin:xmax, :]
#         # cv2.imshow(bbox['name'], cropped)
#         cv2.imwrite("tmp/img%08d.jpg" % counter, cropped)
#         counter = counter + 1
#         result_json.append(box)
#         # cv2.waitKey(1)

with open("../data/gcp-vision.json") as f:
    data_gcp = json.load(f)
# for key in sorted(data.keys()):
#     img = cv2.imread("../../images/"+key)
#     # img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
#     # cv2.imshow('img', img)
#     for bbox in data[key]:
#         box = {'orig_fname': key, "fname": "img%08d.jpg" % counter,
#                "class": bbox['name']}
#         xmin = int(img.shape[1] * float(bbox['ymin']))
#         ymin = int(img.shape[0] * float(bbox['xmin']))
#         xmax = int(img.shape[1] * float(bbox['ymax']))
#         ymax = int(img.shape[0] * float(bbox['xmax']))
#         cropped = img[ymin:ymax, xmin:xmax, :]
#         # cv2.imshow(bbox['name'], cropped)
#         cv2.imwrite("tmp/img%08d.jpg" % counter, cropped)
#         counter = counter + 1
#         result_json.append(box)
#         # cv2.waitKey(1)


with open("../data/data_mod.json") as f:
    data_mnw = json.load(f)

merged = data_mnw

for i in range(len(data_mnw)):
    # print(data_gcp[i].keys(), merged[i].keys())
    # print(data_gcp[i]['fname'])
    # print(data_oid[data_gcp[i]['fname']])
    for k in data_gcp[i]:
        merged[i][k] = data_gcp[i][k]
        merged[i]['objects'] = data_oid[data_gcp[i]['fname']]
    # merged[i] = merged[i].copy().update(data_gcp[i])

# print('='*40, "GCP:")
# print(data_gcp[180])
# print('='*40, "OID:")
# # print(data_oid)
# print('='*40, "MNW:")
# print(data_mnw[180])
# print('='*40)
# print(merged[0])

with open('../data/merged.json', 'w') as f:
    json.dump(merged, f)
