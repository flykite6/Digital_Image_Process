# import numpy as np
from numpy import array,clip,uint8
from numpy.random import rayleigh
def rayleigh_noise(image,var=0.1):
    '''
        添加瑞利噪声
        var : 方差
    '''
    image = array(image/255, dtype=float)
    # 瑞利分布
    noise = rayleigh(var ** 0.5, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = clip(out, low_clip, 1.0)
    out = uint8(out*255)
    return out
