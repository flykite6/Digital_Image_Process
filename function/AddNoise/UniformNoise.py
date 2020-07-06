from numpy import array,clip,uint8
from numpy.random import uniform
def uniform_noise(image,hight=1.0,low=0.0):
    '''
    均匀噪声
    :param hight:采样上界
    :param low:采样下界
    '''
    image = array(image/255, dtype=float)
    # 均匀分布
    noise = uniform(low,hight,image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = clip(out, low_clip, 1.0)
    out = uint8(out*255)
    return out
