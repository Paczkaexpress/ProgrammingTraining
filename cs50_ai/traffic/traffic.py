import cv2
import numpy as np
import os
import sys
import tensorflow as tf
import time

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])
   # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    print("\nFitting the model finished\n")
    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """
    data = tuple()
    images = list()
    labels = list()
    print(os.listdir(data_dir))
    for category in os.listdir(data_dir):
        print(category)

        for image in os.listdir(os.path.join(data_dir, category)):
            # print(os.path.join(data_dir, category, image))
            img = cv2.imread(os.path.join(data_dir, category, image))
            img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT))
            images.append(img)
            labels.append(int(category))
            # print(img)
            # cv2.imshow('test',cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
            # cv2.waitKey(1)
            # if(len(images[-1]) != 30 and len(images[-1][0]) != 30 and len(images[-1][0][0]) != 3):
            #     print("Fuck: {} {} {}".format(len(images[0]),len(images[0][0]),len(images[-1][0][0])))
    
    return images, labels

def get_model():
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """

    model = None

#  experiments with number of filters

    # #  results epoch 10: loss: 0.0104 - accuracy: 0.9226 
    # #  results test case: loss: 0.0050 - accuracy: 0.9639
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         100, (3,3), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])


    # #  results epoch 10: loss: loss: 0.0088 - accuracy: 0.9331
    # #  results test case: loss: 0.0054 - accuracy: 0.9632
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         10, (3,3), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0088 - accuracy: 0.9386
    # #  results test case: loss: 0.0044 - accuracy: 0.9680
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (3,3), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

# changing the kernel size
    # #  results epoch 10: loss: 0.0066 - accuracy: 0.9508
    # #  results test case: loss: 0.0041 - accuracy: 0.9722
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0067 - accuracy: 0.9518
    # #  results test case: loss: 0.0043 - accuracy: 0.9728
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (7,7), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0125 - accuracy: 0.9020
    # #  results test case: loss: 0.0064 - accuracy: 0.9624
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (7,7), activation="linear", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

# pooling tests
    # #  results epoch 10: loss: 0.0074 - accuracy: 0.9454
    # #  results test case: loss: 0.0054 - accuracy: 0.9635
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     # tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0071 - accuracy: 0.9506
    # #  results test case: loss: 0.0047 - accuracy: 0.9707
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0082 - accuracy: 0.9377
    # #  results test case: loss: 0.0054 - accuracy: 0.9595
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(4,4)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])
# number of layers
    # #  results epoch 10: loss: 0.0062 - accuracy: 0.9621
    # #  results test case: loss: 0.0075 - accuracy: 0.9566
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     # tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0071 - accuracy: 0.9506
    # #  results test case: loss: 0.0047 - accuracy: 0.9707
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0182 - accuracy: 0.8525
    # #  results test case: loss: 0.0101 - accuracy: 0.9293
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0029 - accuracy: 0.9790
    # #  results test case: loss: 0.0023 - accuracy: 0.9843
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Conv2D(32, (5,5), activation="relu"),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(128, activation="relu"),
    #     tf.keras.layers.Dropout(0.5),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])
    
    #  results epoch 10: loss: 0.0022 - accuracy: 0.9838
    #  results test case: loss: 0.0020 - accuracy: 0.9886
    model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(
            32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
        ),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
        tf.keras.layers.Conv2D(32, (5,5), activation="relu"),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.7),
        tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    ])

    # #  results epoch 10: loss: 0.0021 - accuracy: 0.9877
    # #  results test case: loss: 0.0034 - accuracy: 0.9798
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         32, (5,5), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Conv2D(32, (5,5), activation="relu"),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(300, activation="relu"),
    #     tf.keras.layers.Dense(300, activation="relu"),
    #     tf.keras.layers.Dense(300, activation="relu"),
    #     tf.keras.layers.Dropout(0.7),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    # #  results epoch 10: loss: 0.0050 - accuracy: 0.9659
    # #  results test case: loss: 0.0034 - accuracy: 0.9778
    # model = tf.keras.models.Sequential([
    #     tf.keras.layers.Conv2D(
    #         50, (6,6), activation="relu", input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)
    #     ),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Conv2D(50, (3,3), activation="relu"),
    #     tf.keras.layers.BatchNormalization(),
    #     tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Conv2D(30, (3,3), activation="relu"),
    #     tf.keras.layers.BatchNormalization(),
    #     # tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     # tf.keras.layers.Conv2D(15, (3,3), activation="relu"),
    #     # tf.keras.layers.BatchNormalization(),
    #     # tf.keras.layers.MaxPooling2D(pool_size=(2,2)),
    #     tf.keras.layers.Flatten(),
    #     tf.keras.layers.Dense(200),
    #     tf.keras.layers.Dropout(0.3),
    #     tf.keras.layers.Dense(200),
    #     tf.keras.layers.Dropout(0.7),
    #     tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    # ])

    model.compile(
        optimizer = "adam",
        loss = "binary_crossentropy",
        metrics = ["accuracy"]
    )
    return model

if __name__ == "__main__":
    main()