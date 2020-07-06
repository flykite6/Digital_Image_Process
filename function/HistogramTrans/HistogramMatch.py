from custom.ImageView import childwindow1
from cv2 import cvtColor,COLOR_RGBA2RGB,imread
from numpy import zeros_like,histogram,cumsum

def HisgramMatch(img):
    _, _, colorChannel = img.shape
    if colorChannel == 4:# 4维降为3维
        img = cvtColor(img,COLOR_RGBA2RGB)
        colorChannel = colorChannel -1
    childwindow = childwindow1()
    fname = childwindow.openfile()
    ref = imread(fname) # 读取匹配的图像
    _, _, colorChannel1 = ref.shape
    if colorChannel1 == 4:
        ref = cvtColor(ref, COLOR_RGBA2RGB)
    out = zeros_like(img)
    for i in range(colorChannel):
        print(i)
        hist_img, _ = histogram(img[:, :, i], 256)  # 得到图像的直方图
        hist_ref, _ = histogram(ref[:, :, i], 256)
        cdf_img = cumsum(hist_img)  # 得到图像的累计直方图
        cdf_ref = cumsum(hist_ref)

        for j in range(256):
            tmp = abs(cdf_img[j] - cdf_ref)
            tmp = tmp.tolist()
            idx = tmp.index(min(tmp)) # 得到灰度阶差距最小的下标
            out[:, :, i][img[:, :, i] == j] = idx

    return out
