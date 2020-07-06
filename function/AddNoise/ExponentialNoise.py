# import numpy as np
from numpy import array,random,clip,uint8

def exponential_noise(image, scale = 0.1):
    '''
    指数噪声
    :param scale:指数值
    '''
    image = array(image/255, dtype=float)
    noise = random.exponential(scale,image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = clip(out, low_clip, 1.0)
    out = uint8(out*255)
    return out