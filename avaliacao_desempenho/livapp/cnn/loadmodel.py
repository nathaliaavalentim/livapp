#!/usr/local/bin/python
# -*- coding: latin-1 -*-
import os
import warnings
warnings.filterwarnings('always')
warnings.filterwarnings('ignore')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline  
import seaborn as sns
from sklearn.model_selection import train_test_split
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import applications
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dropout, Flatten, Input, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import random
import cv2 as cv
import os 
import glob
import tempfile
from tensorflow.keras.models  import model_from_json
from tensorflow.keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
IMAGE_WIDTH = 300
IMAGE_HEIGHT = 300
BATCH_SIZE = 16


temp_dir = tempfile.TemporaryDirectory()
os.environ['MPLCONFIGDIR'] = temp_dir.name


# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

loaded_model.compile(optimizer = Nadam(lr = 0.0001) , loss = 'categorical_crossentropy', metrics=['accuracy'])

#path = 'D:/upload/'
path = 'C:/Users/Nathália/eclipse-workspace/mysite/upload/'

mylist = os.listdir(path)

for i in mylist:
# load an image from file
    image = load_img(path+i, target_size=(48, 48))
# convert the image pixels to a numpy array
    image = img_to_array(image)
# reshape data for the model
    image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
# prepare the image for the VGG model
    image = preprocess_input(image)

#Classificando alguns exemplos
    pred = loaded_model.predict(image)
    pred = np.argmax(pred, axis = 1)

    print(i)
    print(pred)
    print(' ')

