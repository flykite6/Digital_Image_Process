from cv2 import cvtColor,COLOR_RGBA2RGB
from numpy import zeros,uint8
from function.GeometricTrans.LargeSmall import *

def mirror(img,rate):
    '''
    实现图像的镜像
    :param img: 要镜像的图像
    :param rate: 图像放缩的比例
    :return: 返回镜像后得到的图像
    '''
    imgInfo = img.shape
    height= imgInfo[0]
    width = imgInfo[1]
    colorChannel = imgInfo[2]
    # 如果图像是RGBA的，则将其转化为RGB
    if colorChannel == 4:
        img = cvtColor(img,COLOR_RGBA2RGB)
        colorChannel = colorChannel -1
    dst = zeros([height, width*2, colorChannel], uint8)
    # 以下循环实现了图像的镜像
    for i in range(height):
        for j in range(width):
            dst[i,j] = img[i,j]
            dst[i,width*2-j-1] = img[i,j]

    for i in range(height):
        dst[i,width] = (0, 0, 255)
    return largeSmall(dst, rate)