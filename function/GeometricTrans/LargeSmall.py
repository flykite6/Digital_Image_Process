# import cv2
from cv2 import resize

def largeSmall(img,rate=100):
    '''
    实现了图像的放缩
    :param img: 要放缩的图像
    :param rate: 图像放缩的比例
    :return: 返回放缩后得到的图像
    '''
    rate = rate / 100
    img_info = img.shape
    image_height = img_info[0]
    image_weight = img_info[1]
    desHeight = int(rate*image_height)
    desWeight = int(rate*image_weight)
    img = resize(img,(desWeight,desHeight))
    return img
