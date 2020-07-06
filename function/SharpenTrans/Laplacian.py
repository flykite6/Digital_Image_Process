# import cv2
# import numpy as np


# laplacian filter
from function.GrayscaleTrans.BGR2GRAY import rgbToGray
from numpy import zeros,sum,clip,float,uint8

def laplacian_filter(img, K_size=3):
	H, W, C = img.shape
	gray = rgbToGray(img)
	# zero padding
	pad = K_size // 2
	out = zeros((H + pad * 2, W + pad * 2), dtype=float)
	out[pad: pad + H, pad: pad + W] = gray.copy().astype(float)
	tmp = out.copy()
	# laplacian kernle
	K = [[0., 1., 0.],[1., -4., 1.], [0., 1., 0.]]
	# filtering
	for y in range(H):
		for x in range(W):
			out[pad + y, pad + x] = sum(K * (tmp[y: y + K_size, x: x + K_size]))
	out = clip(out, 0, 255)
	out = out[pad: pad + H, pad: pad + W].astype(uint8)
	return out