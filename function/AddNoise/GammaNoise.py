# import numpy as np
# import cv2
from numpy import array,random,clip,uint8

def gamma_noise(image, var=0.1):
    '''
    伽马噪声
    :param var: 方差
    '''
    image = array(image/255, dtype=float)
    # 伽马分布
    noise = random.gamma(3,var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = clip(out, low_clip, 1.0)
    out = uint8(out*255)
    return out