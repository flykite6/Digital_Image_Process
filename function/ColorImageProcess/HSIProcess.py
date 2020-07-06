import cv2
import numpy as np


def hsvProcess(img,h_value,s_value,v_value):
    '''
    调节r，g，b的成分比例
    :param img:
    :param h_value: b的比例
    :param s_value: g的比例
    :param v_value: r的比例
    :return:
    '''
    h_value = float(h_value/100)
    s_value = float(s_value/100)
    v_value = float(v_value/100)
    if img.shape[2] == 4:
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    H, S, V = cv2.split(img) # (b,g,r)
    new_pic = cv2.merge([np.uint8(H * h_value), np.uint8(S * s_value), np.uint8(V * v_value)])
    return new_pic




def rgb2hsi(rgb_img,h_value,s_value,i_value):
    h_value = float(h_value / 100)
    s_value = float(s_value / 100)
    i_value = float(i_value / 100)
    if rgb_img.shape[2] == 4:
        img = cv2.cvtColor(rgb_img, cv2.COLOR_RGBA2RGB)
    rows = int(rgb_img.shape[0])
    cols = int(rgb_img.shape[1])
    b, g, r = cv2.split(img)
    # 归一化到[0,1]
    b = b / 255.0
    g = g / 255.0
    r = r / 255.0
    hsi_img = img.copy()
    H, S, I = cv2.split(hsi_img)
    for i in range(rows):
        for j in range(cols):
            # 获得theta值
            num = 0.5 * ((r[i, j]-g[i, j])+(r[i, j]-b[i, j]))
            den = np.sqrt((r[i, j]-g[i, j])**2+(r[i, j]-b[i, j])*(g[i, j]-b[i, j]))
            theta = float(np.arccos(num/den))
            if den == 0:
                H = 0
            elif b[i, j] <= g[i, j]:
                H = theta
            else:
                H = 2*3.14169265 - theta
            min_RGB = min(min(b[i, j], g[i, j]), r[i, j])
            sum = b[i, j]+g[i, j]+r[i, j]
            if sum == 0:
                S = 0
            else:
                S = 1 - 3*min_RGB/sum
            # 归一到0-1之间
            H = H/(2*3.14159265)
            I = sum/3.0
            # 输出HSI图像，扩充到255以方便显示，一般H分量在[0,2pi]之间，S和I在[0,1]之间
            hsi_img[i, j, 0] = H*255
            hsi_img[i, j, 1] = S*255
            hsi_img[i, j, 2] = I*255
    hsi_img[:,:,0] = hsi_img[:,:,0]*h_value
    hsi_img[:,:,1] = hsi_img[:,:,0]*s_value
    hsi_img[:,:,1] = hsi_img[:,:,0]*i_value
    return hsi_img
