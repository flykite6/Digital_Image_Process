# import numpy as np
from numpy import where,uint8
from cv2 import cvtColor,COLOR_RGBA2BGR
# histogram equalization
def hist_equal(img, z_max=255):
	if img.shape == 4:
		img = cvtColor(img,COLOR_RGBA2BGR)
	H, W, C = img.shape
	S = H * W * C * 1.
	out = img.copy()
	sum_h = 0.
	for i in range(1, 255):
		ind = where(img == i)
		sum_h += len(img[ind])
		z_prime = z_max / S * sum_h
		out[ind] = z_prime
	out = out.astype(uint8)
	return out

