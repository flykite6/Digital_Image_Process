import cv2
import numpy as np
import dlib
from matplotlib import pyplot as plt


def idCardPicGenerate(img, type):
    detector = dlib.get_frontal_face_detector() # 返回人脸的矩形框
    # 返回人脸重要的68个点的位置
    landmark_predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')
    if img.shape[2] == 4:
        img = cv2.cvtColor(img,cv2.COLOR_RGBA2BGR)
    imgg = img.copy()
    t = img.shape
    faces = detector(img, 1)
    print(faces)
    mask = np.zeros(img.shape[:2], np.uint8)
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)
    if (len(faces) > 0):
        for k, d in enumerate(faces):
            left = max(int((3 * d.left() - d.right()) / 2), 1)
            top = max(int((3 * d.top() - d.bottom()) / 2) - 50, 1)
            right = min(int((3 * d.right() - d.left()) / 2), t[1])
            bottom = min(int((3 * d.bottom() - d.top()) / 2), t[0])
            rect = (left, top, right, bottom)
            rect_reg = (d.left(), d.top(), d.right(), d.bottom())
            # shape = landmark_predictor(img, d)
            shape = landmark_predictor(img, d)
            print(shape)
    else:
        exit(0)
    # mask会保存明显的背景像素为0，明显的前景像素为1，可能的背景像素为2，可能的前景像素为3
    cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 100,
                cv2.GC_INIT_WITH_RECT)  # 函数返回值为mask,bgdModel,fgdModel
    # 利用mask做模板
    mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')  # 0和2做背景

    # 背景颜色
    bg_color = [(225, 166, 23), (0, 0, 255), (255, 255, 255)]
    img = img * mask2[:, :, np.newaxis]  # 使用蒙板来获取前景区域
    erode = cv2.erode(img, None, iterations=1) # 腐蚀操作
    dilate = cv2.dilate(erode, None, iterations=1) # 膨胀操作
    for i in range(t[0]):  # 高、
        for j in range(t[1]):
            if max(dilate[i, j]) <= 0:
                dilate[i, j] = bg_color[type]
    img = img[rect[1]:rect[3], rect[0]:rect[2]]
    dilate = dilate[rect[1]:rect[3], rect[0]:rect[2]]
    output_im = cv2.resize(dilate, (361, 381))
    return output_im