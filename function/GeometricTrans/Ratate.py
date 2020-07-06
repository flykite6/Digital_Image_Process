from cv2 import getRotationMatrix2D,warpAffine
from math import fabs,sin,radians,cos

def ratate(img,degree=0):
    '''
    实现图像的旋转
    :param img: 需要旋转的图像
    :param degree: 旋转的角度
    :return: 返回旋转后的图像
    '''
    height, width = img.shape[:2]
    # 旋转后的尺寸
    heightNew = int(width * fabs(sin(radians(degree))) + height * fabs(cos(radians(degree))))
    widthNew = int(height * fabs(sin(radians(degree))) + width * fabs(cos(radians(degree))))
    # 获得仿射变换矩阵
    matRotation = getRotationMatrix2D((width / 2, height / 2), degree, 1)
    matRotation[0, 2] += (widthNew - width) / 2
    matRotation[1, 2] += (heightNew - height) / 2
    # 进行仿射变换
    imgRotation = warpAffine(img, matRotation, (widthNew, heightNew), borderValue=(68, 68, 68))
    return imgRotation
