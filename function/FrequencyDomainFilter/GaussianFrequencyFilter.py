
import cv2
import numpy as np
from function.GrayscaleTrans.BGR2GRAY import rgbToGray

# 高斯滤波器模板
def make_transform_matrix(d,image,s1):
    transfor_matrix = np.zeros(image.shape)
    center_point = tuple(map(lambda x: (x - 1) / 2, s1.shape))
    for i in range(transfor_matrix.shape[0]):
        for j in range(transfor_matrix.shape[1]):
            def cal_distance(pa, pb):
                from math import sqrt
                dis = sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
                return dis

            dis = cal_distance(center_point, (i, j))
            transfor_matrix[i, j] = np.exp(-(dis ** 2) / (2 * (d ** 2)))
    return transfor_matrix

def GaussianFilter(image,d,kind):
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    image = rgbToGray(image)
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    s1 = np.log(np.abs(fshift))
    if kind == 2:
        d_matrix = make_transform_matrix(d,image,s1)
    elif kind == 5:
        d_matrix = 1-make_transform_matrix(d,image,s1)
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift*d_matrix)))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1

# # 高斯选择滤波器模板
# def make_select_matrix(d,image,s1,W):
#     transfor_matrix = np.zeros(image.shape)
#     center_point = tuple(map(lambda x:(x-1)/2,s1.shape))
#     for i in range(transfor_matrix.shape[0]):
#         for j in range(transfor_matrix.shape[1]):
#             def cal_distance(pa,pb):
#                 from math import sqrt
#                 dis = sqrt((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)
#                 return dis
#             dis = cal_distance(center_point,(i,j))
#             if dis != 0 and W != 0: # 高斯分布
#                 transfor_matrix[i,j] =1 - np.exp(-(dis**2-d**2)/(2*(dis*W)))
#     return transfor_matrix

# 定义函数，高斯带阻/通滤波模板
def GaussianBand(src, w, d0):
    template = np.zeros(src.shape, dtype=np.float32)  # 构建滤波器
    r, c = src.shape
    for i in np.arange(r):
        for j in np.arange(c):
            distance = np.sqrt((i - r / 2) ** 2 + (j - c / 2) ** 2)
            temp = ((distance**2 - d0**2)/(distance*w+0.00000001))**2
            template[i, j] = 1 - np.exp(-0.5 * temp)
    return template

def GaussianSelectFilter(image,d,W,kind):
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2BGR)
    image = rgbToGray(image)
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)
    s1 = np.log(np.abs(fshift))
    if kind == 2: # 高斯带阻滤波器
        # d_matrix = make_select_matrix(d,image,s1,W)
        d_matrix = GaussianBand(image,W,d)
    elif kind == 5: # 高斯带通滤波器
        # d_matrix = 1-make_select_matrix(d,image,s1,W)
        d_matrix = 1-GaussianBand(image,W,d)
    img_d1 = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift*d_matrix)))
    img_d1 = img_d1 / img_d1.max()
    img_d1 = img_d1 * 255
    img_d1 = img_d1.astype(np.uint8)
    return img_d1



