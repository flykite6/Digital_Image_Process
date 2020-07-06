# import cv2
# import numpy as np
from cv2 import CV_16S,Sobel,convertScaleAbs,addWeighted
from numpy import expand_dims,zeros,float,sum, clip
from function.GrayscaleTrans.BGR2GRAY import *

# sobel filter
def sobel_filter(img, K_size=3):
	if len(img.shape) == 3:
		H, W, C = img.shape
	else:
		img = expand_dims(img, axis=-1)
		H, W, C = img.shape
	# 填充0
	gray = rgbToGray(img) # 灰度化
	pad = K_size // 2
	out = zeros((H + pad * 2, W + pad * 2), dtype=float)
	out[pad: pad + H, pad: pad + W] = gray.copy().astype(float)
	tmp = out.copy()
	out_v = out.copy()
	out_h = out.copy()
	## 水平x方向
	Kx = [[1., 0., -1.], [2., 0., -2.], [1., 0., -1.]]
	## 竖直y方向
	Ky = [[1., 2., 1.],[0., 0., 0.], [-1., -2., -1.]]
	for y in range(H):
		for x in range(W):
			out_v[pad + y, pad + x] = sum(Ky * (tmp[y: y + K_size, x: x + K_size]))
			out_h[pad + y, pad + x] = sum(Kx * (tmp[y: y + K_size, x: x + K_size]))
	out_v = clip(out_v, 0, 255)
	out_h = clip(out_h, 0, 255)
	out_v = out_v[pad: pad + H, pad: pad + W].astype(uint8)
	out_h = out_h[pad: pad + H, pad: pad + W].astype(uint8)
	dst = addWeighted(out_v, 0.5, out_h, 0.5, 0) # 合并两个方向得到的结果
	return dst

def cv2_sobel(img):

	x = Sobel(img, CV_16S, 1, 0)
	y = Sobel(img, CV_16S, 0, 1)

	absX = convertScaleAbs(x)  # 转回unit8
	absY = convertScaleAbs(y)

	dst = addWeighted(absX, 0.5, absY, 0.5, 0)
