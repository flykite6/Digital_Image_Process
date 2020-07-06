import numpy as np
import math
import cv2
# 计算高斯卷积核
def gausskernel(size,sigma=1.0):
    gausskernel=np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm=math.pow(i-1,2)+pow(j-1,2)
            gausskernel[i,j]=math.exp(-norm/(2*math.pow(sigma,2)))   # 求高斯卷积
    sum=np.sum(gausskernel)   # 求和
    kernel=gausskernel/sum   # 归一化
    return kernel

# 高斯滤波
def gaussian_filter(img,size=3,sigma=1.3):
    if img.shape[2] == 4:
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2GRAY)
    h=img.shape[0]
    w=img.shape[1]
    img1=np.zeros((h,w),np.uint8)
    kernel=gausskernel(size,sigma)   # 计算高斯卷积核
    for i in range (1,h-1):
        for j in range (1,w-1):
            sum=0
            for k in range(-1,2):
                for l in range(-1,2):
                    sum+=img[i+k,j+l]*kernel[k+1,l+1]   # 高斯滤波
            img1[i,j]=sum
    return img1