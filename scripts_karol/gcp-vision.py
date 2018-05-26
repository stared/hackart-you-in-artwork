#!/usr/bin/env python

# Copyright 2015 Google, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Draws squares around detected faces in the given image."""

import argparse

from google.cloud import vision
from google.cloud.vision import types
from PIL import Image, ImageDraw
from pprint import pprint
from tqdm import tqdm
from glob import glob

def detect_gcp(face_file, max_results=4):
    """Uses the Vision API to detect faces in the given file.

    Args:
        face_file: A file-like object containing an image with faces.

    Returns:
        An array of Face objects with information about the picture.
    """

    info = dict()

    # [START get_vision_service]
    client = vision.ImageAnnotatorClient()
    # [END get_vision_service]

    content = face_file.read()
    image = types.Image(content=content)

    response = client.label_detection(image=image)
    info['labels'] = [x.description for x in response.label_annotations]

    response = client.image_properties(image=image)
    props = response.image_properties_annotation
    # print('Properties:')

    # print(props.dominant_colors.colors[0])

    info['color'] = {"r": props.dominant_colors.colors[0].color.red,
                     "g": props.dominant_colors.colors[0].color.green,
                     "b": props.dominant_colors.colors[0].color.blue}

    response = client.safe_search_detection(image=image)
    safe = response.safe_search_annotation

    # Names of likelihood from google.cloud.vision.enums
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                       'LIKELY', 'VERY_LIKELY')

    info['safe'] = {"adult": safe.adult, "violence": safe.violence,
                    "medical": safe.medical, "racy": safe.racy,
                    "spoofed": safe.spoof}

    face_annotations = client.face_detection(image=image,
                                             max_results=
                                             max_results).face_annotations

    if len(face_annotations) > 0:
        info['faces'] = []

    for f in face_annotations:
        # bounding_poly = {"xmin":min(f.bounding_poly.vertices[0].x, f.bounding_poly.vertices[0].x,)}
        info['faces'].append({"joy": f.joy_likelihood,
                              "sorrow": f.sorrow_likelihood,
                              "anger": f.anger_likelihood,
                              "surprise": f.surprise_likelihood,
                              "under_exposed": f.under_exposed_likelihood,
                              "blurred": f.blurred_likelihood,
                              "headwear": f.headwear_likelihood})

    # print(info)

    return info

def highlight_faces(image, faces, output_filename):
    """Draws a polygon around the faces, then saves to output_filename.

    Args:
      image: a file containing the image with the faces.
      faces: a list of faces found in the file. This should be in the format
          returned by the Vision API.
      output_filename: the name of the image file to be created, where the
          faces have polygons drawn around them.
    """
    im = Image.open(image)
    draw = ImageDraw.Draw(im)

    for face in faces:
        box = [(vertex.x, vertex.y)
               for vertex in face.bounding_poly.vertices]
        draw.line(box + [box[0]], width=5, fill='#00ff00')

    im.save(output_filename)


def main(input_filename, max_results):
    result = None
    with open(input_filename, 'rb') as image:
        result = detect_gcp(image, max_results)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'images_dir', help='directory with jpg images')
    args = parser.parse_args()

    images = sorted(glob(args.images_dir + "/*.jpg"))

    result_json = dict()
    for img in tqdm(images):
        result_json[img.split('/')[-1]] = main(img, 1000)
    print(result_json)
