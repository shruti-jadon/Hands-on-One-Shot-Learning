import numpy as np
from scipy import misc
import os

dataset = []
examples = []
# images_background
data_root = "./data/"
alphabets = os.listdir(data_root + "images_background")
for alphabet in alphabets:
    characters = os.listdir(os.path.join(data_root, "images_background", alphabet))
    for character in characters:
        files = os.listdir(os.path.join(data_root, "images_background", alphabet, character))
        examples = []
        for img_file in files:
            img = misc.imresize(
                                misc.imread(os.path.join(data_root, "images_background", alphabet, character, img_file)), [28, 28])
            examples.append(img) # example level append, making dim as 20X28X28
        dataset.append(examples) # character level append, making dim as (20*30)X20X28X28

# images_evaluation
data_root = "./data/"
alphabets = os.listdir(data_root + "images_evaluation")
for alphabet in alphabets:
    characters = os.listdir(os.path.join(data_root, "images_evaluation", alphabet))
    for character in characters:
        files = os.listdir(os.path.join(data_root, "images_evaluation", alphabet, character))
        examples = []
        for img_file in files:
            img = misc.imresize(
                                misc.imread(os.path.join(data_root, "images_evaluation", alphabet, character, img_file)), [28, 28])
            examples.append(img)
        dataset.append(examples) # character level append, making dim as (n)X20X28X28

np.save(data_root + "dataset.npy", np.asarray(dataset))
