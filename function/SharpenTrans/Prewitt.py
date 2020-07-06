# import cv2
# import numpy as np
from cv2 import addWeighted
from numpy import zeros,expand_dims,float,uint8,sum,clip
from function.GrayscaleTrans.BGR2GRAY import rgbToGray

# prewitt filter
def prewitt_filter(img, K_size=3):
	gray = rgbToGray(img)
	if len(img.shape) == 3:
		H, W, C = img.shape
	else:
		img = expand_dims(img, axis=-1)
		H, W, C = img.shape
	# 填充0
	pad = K_size // 2
	out = zeros((H + pad * 2, W + pad * 2), dtype=float)
	out[pad: pad + H, pad: pad + W] = gray.copy().astype(float)
	tmp = out.copy()
	out_v = out.copy()
	out_h = out.copy()
	## prewitt 水平方向的核
	Kv = [[-1., -1., -1.],[0., 0., 0.], [1., 1., 1.]]
	## prewitt 竖直方向的核
	Kh = [[-1., 0., 1.],[-1., 0., 1.],[-1., 0., 1.]]
	# filtering
	for y in range(H):
		for x in range(W):
			out_v[pad + y, pad + x] = sum(Kv * (tmp[y: y + K_size, x: x + K_size]))
			out_h[pad + y, pad + x] = sum(Kh * (tmp[y: y + K_size, x: x + K_size]))
	out_v = clip(out_v, 0, 255)
	out_h = clip(out_h, 0, 255)
	out_v = out_v[pad: pad + H, pad: pad + W].astype(uint8)
	out_h = out_h[pad: pad + H, pad: pad + W].astype(uint8)
	dst = addWeighted(out_v, 0.5, out_h, 0.5, 0)
	return  dst

# 读取图像
# img = cv2.imread('../pic/boy.png')
# prewitt_filter(img)