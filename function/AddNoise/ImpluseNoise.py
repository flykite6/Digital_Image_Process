from random import random
from numpy import zeros,uint8,random
import cv2

def impluse_noise(image,prob=0.1):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = zeros(image.shape,uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

