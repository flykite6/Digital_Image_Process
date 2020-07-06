# import numpy as np
# import cv2
from numpy import array,random,clip,uint8

def gasuss_noise(image, var=0.1, mean=0):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = array(image/255, dtype=float)
    # 高斯分布
    noise = random.normal(mean, var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = clip(out, low_clip, 1.0)
    out = uint8(out*255)
    return out
