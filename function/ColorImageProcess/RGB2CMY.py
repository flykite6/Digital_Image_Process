import cv2
from function.ColorImageProcess.HSIProcess import hsvProcess


def rgb2cmy(img,H,S,V):
    if img.shape[2] == 4:
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2RGB)
    (b,g,r) = cv2.split(img)
    b = 1 - b/b.max()
    g = 1 - g/g.max()
    r = 1 - r/r.max()
    img_1 = cv2.merge([255*b,255*g,255*r])
    img_result = hsvProcess(img_1,H,S,V)
    return img_result


