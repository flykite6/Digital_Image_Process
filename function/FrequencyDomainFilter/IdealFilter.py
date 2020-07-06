import numpy as np
import cv2
from function.GrayscaleTrans.BGR2GRAY import rgbToGray

def make_transform_matrix(d,image,s1):
    """
        构建理想低通滤波器
        :param d: 滤波器半径
        :param image: 图像的傅里叶变换
        :return:
    """
    transfor_matrix = np.zeros(image.shape)
    center_point = tuple(map(lambda x:(x-1)/2,s1.shape))
    for i in range(transfor_matrix.shape[0]):
        for j in range(transfor_matrix.shape[1]):
            def cal_distance(pa,pb):
                from math import sqrt
                dis = sqrt((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)
                return dis
            dis = cal_distance(center_point,(i,j))
            if dis <= d:
                transfor_matrix[i,j]=1
            else:
                transfor_matrix[i,j]=0
    return transfor_matrix

def idealFilter(img,r,kind):
    '''
    理想滤波器
    :param img: 输入图像
    :param r: 滤波器半径
    :param kind: 滤波器类型
    :return: 滤波后的图像
    '''
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR) # 四维转三维
    img = rgbToGray(img) # 灰度化
    f = np.fft.fft2(img)  # 傅里叶变换
    fshift = np.fft.fftshift(f) # 将低频部分移到中心
    # 取绝对值：将复数变化成实数
    # 取对数的目的为了将数据变化到0-255
    s1 = np.log(np.abs(fshift))
    # d1 = make_transform_matrix(r, fshift, s1)
    if kind == 0: # 理想低通滤波
        d1 = make_transform_matrix(r, fshift, s1)
    elif kind == 3: # 理想高通滤波
        d1 = 1-make_transform_matrix(r, fshift, s1)
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * d1)))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1


def make_select_matrix(d,image,s1,W):
    """
        构建理想选择滤波器
        :param d: 滤波器半径
        :param image: 图像的傅里叶变换
        :return:
    """
    transfor_matrix = np.zeros(image.shape)
    center_point = tuple(map(lambda x:(x-1)/2,s1.shape))
    for i in range(transfor_matrix.shape[0]):
        for j in range(transfor_matrix.shape[1]):
            def cal_distance(pa,pb):
                from math import sqrt
                dis = sqrt((pa[0]-pb[0])**2+(pa[1]-pb[1])**2) # 计算两点之间距离
                return dis
            dis = cal_distance(center_point,(i,j))
            # if dis <= d + W/2 and dis >= d - W/2:
            if dis <= d + W and dis >= d:
                transfor_matrix[i,j]=0
            else:
                transfor_matrix[i,j]=1
    return transfor_matrix

def idealSelectFilter(img,r,W,kind):
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    img = rgbToGray(img)
    # 傅里叶变换
    f = np.fft.fft2(img)
    # 将低频部分移到中心
    fshift = np.fft.fftshift(f)
    # 取绝对值：将复数变化成实数
    # 取对数的目的为了将数据变化到0-255
    s1 = np.log(np.abs(fshift))
    if kind == 0: # 理想带阻滤波器
        d1 = make_select_matrix(r, fshift, s1, W)
    elif kind == 3: # 理想带通滤波器
        d1 = 1-make_select_matrix(r, fshift, s1, W)
    # 与模板相乘后再傅里叶逆变换
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * d1)))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1

def make_NotchFilter_matrix(d,image,s1):
    """
        构建理想陷波滤波器
        :param d: 滤波器半径
        :param image: 图像的傅里叶变换
        :return:
    """
    transfor_matrix = np.zeros(image.shape)
    # center_point = tuple(map(lambda x:(x-1)/2,s1.shape))
    center_point_1 = (s1.shape[0]/4,s1.shape[1]/2)
    center_point_2 = (3*s1.shape[0]/4,s1.shape[1]/2)
    for i in range(transfor_matrix.shape[0]):
        for j in range(transfor_matrix.shape[1]):
            def cal_distance(pa,pb):
                from math import sqrt
                dis = sqrt((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)
                return dis
            dis_1 = cal_distance(center_point_1,(i,j))
            dis_2 = cal_distance(center_point_2,(i,j))
            # if dis <= d + W/2 and dis >= d - W/2:
            # if dis <= d + W and dis >= d:
            if dis_1 <= d or dis_2 <= d:
                transfor_matrix[i,j]=0
            else:
                transfor_matrix[i,j]=1
    return transfor_matrix

def idealNotchFilter(img,r,kind):
    img = cv2.cvtColor(img, cv2.COLOR_RGBA2BGR)
    img = rgbToGray(img)
    # 傅里叶变换
    f = np.fft.fft2(img)
    # 将低频部分移到中心
    fshift = np.fft.fftshift(f)
    # fshift = fshift.astype(np.uint8)
    # 取绝对值：将复数变化成实数
    # 取对数的目的为了将数据变化到0-255
    s1 = np.log(np.abs(fshift))
    if kind == 6:
        d1 = make_NotchFilter_matrix(r, fshift, s1)
    elif kind == 7:
        d1 = 1-make_NotchFilter_matrix(r, fshift, s1)
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift * d1)))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1
