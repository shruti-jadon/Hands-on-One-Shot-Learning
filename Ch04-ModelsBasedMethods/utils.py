from scipy.misc import imresize
from matplotlib.pyplot import imread
from os import listdir
from os.path import splitext
from random import seed,shuffle
from time import time
from numpy import zeros

def load_image(path,shape=False):
    readed_img = imread(path)
    if shape:
        readed_img = imresize(readed_img,shape)
    return readed_img

def extend_children(path,ftype=False):
    allpaths = [path+'/'+child for child in listdir(path) if '.DS_Store' not in child]
    if ftype != False:
        ret = []
        for v in allpaths:
            if splitext(v)[1] == ftype:
                ret.append(v)
    else:
        ret=allpaths    
    return ret

def extend_generation(paths,ftype=False):
    ret = []
    for path in paths:
        ret += extend_children(path,ftype)
    return ret

def shuffle_xy(x,y,shuffleseed=False):
    if shuffleseed:
        seed(shuffleseed)
    shuffler = list(range(len(x)))
    shuffle(shuffler)
    new_x = [x[i] for i in shuffler]
    new_y = [y[i] for i in shuffler]
    return new_x,new_y

def one_hot(index,cols):
    one_hot_vector = [0 for _ in range(cols)]
    one_hot_vector[index] = 1
    return one_hot_vector