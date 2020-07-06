from math import pow
from cv2 import normalize,NORM_MINMAX,convertScaleAbs
from numpy import uint8,zeros,float32
def gammaTranform(c,gamma,image):
    '''
    图像的伽马变换（y = c*r^gamma）
    :param c:
    :param gamma:
    :param image:输入图像
    :return:
    '''
    h,w,d = image.shape[0],image.shape[1],image.shape[2]
    new_img = zeros((h,w,d),dtype=float32)
    for i in range(h):
        for j in range(w):
            new_img[i,j,0] = c*pow(image[i, j, 0], gamma)
            new_img[i,j,1] = c*pow(image[i, j, 1], gamma)
            new_img[i,j,2] = c*pow(image[i, j, 2], gamma)
    normalize(new_img,new_img,0,255,NORM_MINMAX)
    new_img = convertScaleAbs(new_img)
    output_imgae = new_img.astype(uint8)
    return output_imgae