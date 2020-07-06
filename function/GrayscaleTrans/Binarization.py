from function.GrayscaleTrans.BGR2GRAY import *

def binarization(img, th=128):
    '''
    实现了图像的二值化
    :param img: 输入图像
    :param th: 阈值
    :return: 返回二值图像
    '''
    _, _, colorChannel = img.shape
    if colorChannel != 1:
        img = rgbToGray(img)
    img[img < th] = 0
    img[img >= th] = 255
    return img