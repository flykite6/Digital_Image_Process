# import numpy as np
from numpy import copy,max,uint8
def image_reverse(input_image):
    '''
    图像反转
    :param input_image: 原图像
    :return: 反转后的图像
    '''
    input_image_cp = copy(input_image) # 输入图像的副本

    pixels_value_max = max(input_image_cp) # 输入图像像素的最大值

    output_imgae = pixels_value_max - input_image_cp # 输出图像

    output_imgae = output_imgae.astype(uint8)

    return output_imgae