import cv2

from function.GrayscaleTrans.BGR2GRAY import rgbToGray
from function.ColorImageProcess.HSIProcess import hsvProcess


def pseudoColorTrans(img,H,S,V,type):
    if img.shape == 4:
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)
    img_gray = rgbToGray(img)
    if type == 0:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_AUTUMN)
    elif type == 1:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_BONE)
    elif type == 2:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_JET)
    elif type == 3:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_WINTER)
    elif type == 4:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_RAINBOW)
    elif type == 5:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_OCEAN)
    elif type == 6:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_SUMMER)
    elif type == 7:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_SPRING)
    elif type == 8:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_COOL)
    elif type == 9:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_HSV)
    elif type == 10:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_PINK)
    elif type == 11:
        img_color = cv2.applyColorMap(img_gray, cv2.COLORMAP_HOT)
    img_color = hsvProcess(img_color,H,S,V)
    return img_color


# img_gray = cv2.imread("../pic/beach.png",cv2.IMREAD_GRAYSCALE)
# img_color = cv2.applyColorMap(img_gray,cv2.COLORMAP_JET)
# img = cv2.imread('../pic/beach.png')
# img_gray = pseudoColorTrans(img,type)
# cv2.imshow('img_color',img_gray)
# cv2.waitKey(0)
# cv2.imshow('img_color',img_color)
# cv2.waitKey(0)