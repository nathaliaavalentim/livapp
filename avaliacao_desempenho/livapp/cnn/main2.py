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
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Nadam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dropout, Flatten, Input, Dense
from tensorflow.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
import random
#import tensorflow as tf
import cv2 as cv
import os 
import glob
import tempfile
temp_dir = tempfile.TemporaryDirectory()
os.environ['MPLCONFIGDIR'] = temp_dir.name

#Lendo e tratando os dados
satisfied_dir = glob.glob(os.path.join('emotions/satisfied/', '*'))
unsatisfied_dir = glob.glob(os.path.join('emotions/unsatisfied/', '*'))


X_path = satisfied_dir+unsatisfied_dir
X = []
for f in X_path:
    X.append(np.array(cv.resize(cv.imread(f), (224,224), interpolation = cv.INTER_AREA))) 
    
X = np.array(X)
X = X / 255


l_satisfied = np.zeros(len(satisfied_dir))
l_unsatisfied = np.ones(len(unsatisfied_dir))
y = np.concatenate((l_satisfied, l_unsatisfied))
y = to_categorical(y, 2)


X_train, X_val, y_train, y_val = train_test_split(X, y, test_size = 0.2, random_state=42)


#Para evitar problemas de overfitting, usamos o ImageDataGenerator.
datagen = ImageDataGenerator(
        zoom_range = 0.1, # Aleatory zoom
        rotation_range= 15, 
        width_shift_range=0.1,  # horizontal shift
        height_shift_range=0.1,  # vertical shift
        horizontal_flip=True,  
        vertical_flip=True)
datagen.fit(X_train)


#TransferLearning
vgg = tf.keras.applications.VGG16(input_shape=(224,224,3), include_top = False, weights= 'imagenet')


x = vgg.output
x = Flatten()(x)
x = Dense(3078,activation='relu')(x) 
x = Dropout(0.5)(x)
x = Dense(256,activation='relu')(x) 
x = Dropout(0.2)(x)
out = Dense(2,activation='softmax')(x)
tf_model=Model(inputs=vgg.input,outputs=out)
for layer in tf_model.layers[:20]:
    layer.trainable=False


tf_model.compile(optimizer = Nadam(lr = 0.0001) , loss = 'categorical_crossentropy', metrics=['accuracy'])

#Treinando o Modelo
history = tf_model.fit(X_train, y_train, batch_size = 1, epochs = 30, initial_epoch = 0, validation_data = (X_val, y_val))


#Classificando alguns exemplos
pred = tf_model.predict(X_val)
pred = np.argmax(pred, axis = 1)


print(y_val)
print('')
print(pred)

#Salvando o Modelo
# serializar modelo para JSON
model_json = tf_model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serializar pesos para HDF5
tf_model.save_weights("model.h5")
print("Saved model to disk")