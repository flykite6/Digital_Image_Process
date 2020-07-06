from numpy import uint8

def rgbToGray(img):
	'''
	彩色图像灰度化
	:param img: 输入彩色图像
	:return: 输出灰度图像
	'''
	# 得到(r,g,b)三通道
	b = img[:, :, 0].copy()
	g = img[:, :, 1].copy()
	r = img[:, :, 2].copy()
	# 灰度化
	out = 0.2126 * r + 0.7152 * g + 0.0722 * b
	out = out.astype(uint8)
	return out


