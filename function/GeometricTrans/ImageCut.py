from cv2 import selectROI
from function.GeometricTrans.LargeSmall import largeSmall

def cut(img,rate):
    '''
    实现图像的剪切
    :param img:要剪切的图像
    :param rate: 图像放缩的比例
    :return: 返回剪切得到的图像
    '''
    # 得到手动裁剪的矩形区域
    bbox = selectROI(img, False)
    cut = img[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
    return largeSmall(cut, rate)
