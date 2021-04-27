import os
import sys
import random
import math
import numpy as np
import skimage.io
import matplotlib
import matplotlib.pyplot as plt

import coco
import utils
import model as modellib
import visualize
from config import Config

# Root directory of the project
ROOT_DIR = os.getcwd()

# Directory to save logs and trained model
MODEL_DIR = os.path.join(ROOT_DIR, "logs")

# Local path to trained weights file
MODEL_WEIGHT_PATH = os.path.join(ROOT_DIR, "mask_rcnn_val_all.h5")  # 这里输入模型权重的路径
# Download COCO trained weights from Releases if needed
if not os.path.exists(MODEL_WEIGHT_PATH):
    utils.download_trained_weights(MODEL_WEIGHT_PATH)

# Directory of images to run detection on
IMAGE_DIR = os.path.join(ROOT_DIR, "samples\\balloon\\datasets\\balloon\\val2")  # 这是输入你要预测图片的路径


class somethingConfig(Config):
    """Configuration for training on MS COCO.
    Derives from the base Config class and overrides values specific
    to the COCO dataset.
    """
    # Give the configuration a recognizable name
    NAME = "something"

    # We use a GPU with 12GB memory, which can fit two images.
    # Adjust down if you use a smaller GPU.
    IMAGES_PER_GPU = 2

    # Uncomment to train on 8 GPUs (default is 1)
    # GPU_COUNT = 8

    # Number of classes (including background)
    NUM_CLASSES = 1 + 5  # COCO has 80 classes


class InferenceConfig(somethingConfig):
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1


config = InferenceConfig()
# Create model object in inference mode.
model = modellib.MaskRCNN(mode="inference", model_dir=MODEL_DIR, config=config)

# Load weights trained on MS-COCO
model.load_weights(MODEL_WEIGHT_PATH, by_name=True)

# COCO Class names
# Index of the class in the list is its ID. For example, to get ID of
# the teddy bear class, use: class_names.index('teddy bear')
class_names = ['BG', 'person', 'book', 'chair', 'bottle', 'sports bag']

# Load a random image from the images folder
file_names = next(os.walk(IMAGE_DIR))[2]
for x in range(len(file_names)):
    image = skimage.io.imread(os.path.join(IMAGE_DIR, file_names[x]))

    # Run detection
    results = model.detect([image], verbose=1)

    # Visualize results
    r = results[0]
    visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'],
                                class_names, r['scores'])
