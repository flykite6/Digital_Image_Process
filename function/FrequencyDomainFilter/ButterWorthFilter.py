
import cv2
import numpy as np
from function.GrayscaleTrans.BGR2GRAY import rgbToGray


def make_transform_matrix(image,d,s1,n):
    transfor_matrix = np.zeros(image.shape)
    center_point = tuple(map(lambda x: (x - 1) / 2, s1.shape))
    for i in range(transfor_matrix.shape[0]):
        for j in range(transfor_matrix.shape[1]):
            def cal_distance(pa, pb):
                from math import sqrt
                dis = sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
                return dis

            dis = cal_distance(center_point, (i, j))
            transfor_matrix[i, j] = 1 / ((1 + (dis / d)) ** (2 * n))
    return transfor_matrix


def butterworthFilter(image, d, n,kind):
    '''
    巴特沃斯低通滤波器
    :param image: 输入图像
    :param d: 滤波半径
    :param n: 阶数
    :return:
    '''
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    image = rgbToGray(image)
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    s1 = np.log(np.abs(fshift))
    if kind == 1:
        d_matrix = make_transform_matrix(image,d,s1,n)
    elif kind == 4:
        d_matrix = 1-make_transform_matrix(image, d, s1, n)
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * d_matrix)))
    # 高通滤波
    # img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * (1-d_matrix))))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1


# 定义函数，巴特沃斯带阻/通滤波模板
def ButterworthBand(src, w, d0, n):
    template = np.zeros(src.shape, dtype=np.float32)  # 构建滤波器
    r, c = src.shape
    for i in np.arange(r):
        for j in np.arange(c):
            distance = np.sqrt((i - r / 2) ** 2 + (j - c / 2) ** 2)
            # 巴特沃斯分布
            template[i, j] = 1/(1+(distance*w/(distance**2 - d0**2))**(2*n))
    return template


def butterworthSelectFilter(image, d, n,W,kind):
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    image = rgbToGray(image) # 图像灰度化
    f = np.fft.fft2(image) # 图像的傅里叶变换
    fshift = np.fft.fftshift(f) # 将低频移动到中心
    s1 = np.log(np.abs(fshift))
    if kind == 1: # 巴特沃斯带阻滤波器
        d_matrix = ButterworthBand(image,W,d,n)
    elif kind == 4: # 巴特沃斯带通滤波器
        d_matrix = 1-ButterworthBand(image, W, d, n)
    #  与模板相乘后再傅里叶逆变换
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * d_matrix)))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1
