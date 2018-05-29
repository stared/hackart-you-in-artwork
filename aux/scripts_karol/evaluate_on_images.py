"""Evaluate on all images in directory."""
import numpy as np
import os
import json
import sys
import cv2
import tensorflow as tf
from PIL import Image
from glob import glob
from tqdm import tqdm
from utils import label_map_util
from utils import visualization_utils as vis_util

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

if len(sys.argv) != 6:
    print("Usage:\n%s  path/to/frozen_inference_graph.pb  path/to/labels.pbtxt\
NUM_CLASSES  THRESH  path/to/images_dir" % sys.argv[0])
    exit(1)

PATH_TO_CKPT = sys.argv[1]
PATH_TO_LABELS = sys.argv[2]
NUM_CLASSES = int(sys.argv[3])
THRESH = float(sys.argv[4])
VIDEOS_DIR = sys.argv[5]

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
    """Load image into numpy array."""
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


TEST_IMAGE_PATHS = sorted(glob(VIDEOS_DIR+'/*.jpg'))

counter = 0

with detection_graph.as_default():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    with tf.Session(graph=detection_graph, config=config) as sess:
        image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
        detection_boxes = detection_graph.get_tensor_by_name(
            'detection_boxes:0')
        detection_scores = detection_graph.get_tensor_by_name(
            'detection_scores:0')
        detection_classes = detection_graph.get_tensor_by_name(
            'detection_classes:0')
        num_detections = detection_graph.get_tensor_by_name('num_detections:0')

        results = dict()

        for image_path in tqdm(list(TEST_IMAGE_PATHS)):
            base_name = image_path.split('/')[-1][:-4]
            image = Image.open(image_path)
            image_np = load_image_into_numpy_array(image)
            image_np_expanded = np.expand_dims(image_np, axis=0)
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores,
                 detection_classes, num_detections],
                feed_dict={image_tensor: image_np_expanded})
            image_np = cv2.cvtColor(image_np, cv2.COLOR_BGR2RGB)

            objects = []
            for s, c, b in zip(scores[0], classes[0], boxes[0]):
                if s > THRESH:
                    b = list(b)

                    objects.append({"prob": s,
                                    "name": str(category_index[c]['name']),
                                    "xmin": b[0], "ymin": b[1],
                                    "xmax": b[2], "ymax": b[3]})

            results[image_path.split('/')[-1]] = objects

            # Visualization of the results of a detection.
            vis_util.visualize_boxes_and_labels_on_image_array(
              image_np,
              np.squeeze(boxes),
              np.squeeze(classes).astype(np.int32),
              np.squeeze(scores),
              category_index,
              min_score_thresh=THRESH,
              use_normalized_coordinates=True,
              line_thickness=8)
            cv2.imwrite('%s.jpg' % base_name, image_np)
            counter = counter+1
        print(results)
        with open('oidv3.json', 'w') as f:
            json.dump(results, f)
