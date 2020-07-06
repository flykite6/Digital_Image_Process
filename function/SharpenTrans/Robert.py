# import cv2
# import numpy as np
# import matplotlib.pyplot as plt
from cv2 import convertScaleAbs,addWeighted,cvtColor,COLOR_BGR2GRAY,CV_16S,filter2D
from function.GrayscaleTrans.BGR2GRAY import rgbToGray


def robert(img):
    img1 = rgbToGray(img)
    img2 = rgbToGray(img)
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    r, c = img1.shape
    # r_sunnzi = [[-1, -1], [1, 1]]
    r_sunnzi_x = [[-1, 0], [0, 1]]
    r_sunnzi_y = [[0, -1], [1, 0]]
    for x in range(r):
        for y in range(c):
            if (y + 2 <= c) and (x + 2 <= r):
                imgChild = img1[x:x + 2, y:y + 2]
                list_robert = r_sunnzi_x * imgChild
                img1[x, y] = abs(list_robert.sum())  # 求和加绝对值
    for x in range(r):
        for y in range(c):
            if (y + 2 <= c) and (x + 2 <= r):
                imgChild = img2[x:x + 2, y:y + 2]
                list_robert = r_sunnzi_y * imgChild
                img2[x, y] = abs(list_robert.sum())  # 求和加绝对值
    # 转uint8
    absX = convertScaleAbs(img1)
    absY = convertScaleAbs(img2)
    result = addWeighted(absX, 0.5, absY, 0.5, 0)
    # result = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    # cv2.imshow("result",result)
    # cv2.waitKey(0)
    return result


def cv2_robert(img):
    # lenna_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # 灰度化处理图像
    grayImage = cvtColor(img, COLOR_BGR2GRAY)

    # Roberts算子
    kernelx = np.array([[-1, 0], [0, 1]], dtype=int)
    kernely = np.array([[0, -1], [1, 0]], dtype=int)
    x = filter2D(grayImage, CV_16S, kernelx)
    y = filter2D(grayImage, CV_16S, kernely)
    # 转uint8
    absX = convertScaleAbs(x)
    absY = convertScaleAbs(y)
    result = addWeighted(absX, 0.5, absY, 0.5, 0)
    return result
    #
    # # 显示图形
    # titles = [u'原始图像', u'Roberts算子']
    # images = [lenna_img, Roberts]
    # for i in range(2):
    #     plt.subplot(1, 2, i + 1), plt.imshow(images[i], 'gray')
    #     plt.title(titles[i])
    #     plt.xticks([]), plt.yticks([])
    # plt.show()

# 读取图像
# img = cv2.imread('../pic/boy.png')
# robert(img)
# cv2_robert(img)
