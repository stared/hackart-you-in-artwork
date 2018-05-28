import json
# import cv2
import webcolors


def closest_colour(requested_colour):
    min_colours = {}
    for key, name in webcolors.css3_hex_to_names.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_colour[0]) ** 2
        gd = (g_c - requested_colour[1]) ** 2
        bd = (b_c - requested_colour[2]) ** 2
        min_colours[(rd + gd + bd)] = name
    return min_colours[min(min_colours.keys())]


def get_colour_name(requested_colour):
    try:
        closest_name = actual_name = webcolors.rgb_to_name(requested_colour)
    except ValueError:
        closest_name = closest_colour(requested_colour)
        actual_name = None
    return actual_name, closest_name

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
    rgb = merged[i]['color']

    requested_colour = (int(float(rgb['r'])), int(float(rgb['g'])),
                        int(float(rgb['b'])))

    actual_name, closest_name = get_colour_name(requested_colour)
    merged[i]['color']['name'] = closest_name

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
