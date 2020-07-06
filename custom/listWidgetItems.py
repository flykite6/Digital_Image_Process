from PyQt5.QtWidgets import QListWidgetItem
from flags import *

# 功能区引用
# 几何变换
from function.GeometricTrans.Ratate import ratate
from function.GeometricTrans.ImageCut import cut
from function.GeometricTrans.Mirror import mirror
from function.GeometricTrans.LargeSmall import largeSmall
# 灰度变换
from function.GrayscaleTrans.Reverse import image_reverse
from function.GrayscaleTrans.GammaTrans import gammaTranform
from function.GrayscaleTrans.Binarization import binarization
from function.GrayscaleTrans.BGR2GRAY import rgbToGray
# 直方图处理
from function.HistogramTrans.Equalize import hist_equal
from function.HistogramTrans.HistogramMatch import HisgramMatch
# 平滑处理
from function.SmoothingTrans.GaussianFilter import gaussian_filter
from function.SmoothingTrans.MeanFilter import mean_filter
from function.SmoothingTrans.MedianFilter import median_filter
# 锐化处理
from function.SharpenTrans.SobelFilter import sobel_filter
from function.SharpenTrans.Robert import robert
from function.SharpenTrans.Laplacian import laplacian_filter
from function.SharpenTrans.Prewitt import prewitt_filter
# 加性噪声
from function.AddNoise.GasussNoise import gasuss_noise
from function.AddNoise.ImpluseNoise import impluse_noise
from function.AddNoise.RayleighNoise import rayleigh_noise
from function.AddNoise.GammaNoise import gamma_noise
from function.AddNoise.UniformNoise import uniform_noise
from function.AddNoise.ExponentialNoise import exponential_noise
# 频域滤波 | 选择滤波
from function.FrequencyDomainFilter.ButterWorthFilter import butterworthSelectFilter, butterworthFilter
from function.FrequencyDomainFilter.IdealFilter import idealFilter,idealSelectFilter,idealNotchFilter
from function.FrequencyDomainFilter.GaussianFrequencyFilter import GaussianFilter,GaussianSelectFilter
# 彩色图像处理
from function.ColorImageProcess.HSIProcess import hsvProcess, rgb2hsi
from function.ColorImageProcess.RGB2CMY import rgb2cmy
from function.ColorImageProcess.PseudoColorTrans import pseudoColorTrans
# 证件照生成
from function.IdCardPicGenerate.IdCardPicGenerate import idCardPicGenerate

class MyItem(QListWidgetItem):
    def __init__(self, name=None, parent=None):
        super(MyItem, self).__init__(name, parent=parent)

    def get_params(self):
        protected = [v for v in dir(self) if v.startswith('_') and not v.startswith('__')]
        param = {}
        for v in protected:
            param[v.replace('_', '', 1)] = self.__getattribute__(v)
        return param

    def update_params(self, param):
        for k, v in param.items():
            if '_' + k in dir(self):
                self.__setattr__('_' + k, v)


class GeometricTransItem(MyItem):
    def __init__(self, parent=None):
        super(GeometricTransItem, self).__init__(' 几何变换 ', parent=parent)
        self._kind = 0
        self._rate = 100

    def __call__(self, img):
        if self._kind == 0:
            img = largeSmall(img,self._rate)
        elif self._kind == 1:
            img = mirror(img,self._rate)
        elif self._kind == 2:
            img = ratate(img,self._rate)
        elif self._kind == 3:
            img = cut(img,self._rate)
            # img = cut(img)

        return img

class GrayingItem(MyItem):
    def __init__(self, parent=None):
        super(GrayingItem, self).__init__(' 灰度变换 ', parent=parent)
        self._kind = RBG2GRAY
        self._c_value = 1
        self._γ_value = 3.0

    def __call__(self, img):
        if self._kind == 0:
            img = rgbToGray(img)
        elif self._kind == 1:
            img = image_reverse(img)
        elif self._kind == 2:
            img = binarization(img)
        elif self._kind == 3:
            img = gammaTranform(self._c_value,self._γ_value,img)
        return img


class EqualizeItem(MyItem):
    def __init__(self, parent=None):
        super().__init__(' 直方图处理 ', parent=parent)
        self._kind = 0

    def __call__(self, img):
        if self._kind == 0:
            img = hist_equal(img)
        elif self._kind == 1:
            img = HisgramMatch(img)
        return img


class FilterItem(MyItem):

    def __init__(self, parent=None):
        super().__init__('平滑处理', parent=parent)
        self._ksize = 3
        self._kind = 0
        self._sigma = 1

    def __call__(self, img):
        if self._kind == 0:
            img = cv2.blur(img, (self._ksize, self._ksize))
            # img = mean_filter(img,self._ksize)
        elif self._kind == 1:
            # cv2实现的中值滤波
            img = cv2.medianBlur(img, self._ksize)
            # python实现的中值滤波
            # img = median_filter(img, self._ksize)
        elif self._kind == 2:
            # img = cv2.GaussianBlur(img, (self._ksize, self._ksize), self._sigma)
            img = gaussian_filter(img,self._ksize,self._sigma)

        return img


class SharpenItem(MyItem):
    def __init__(self, parent=None):
        super().__init__('锐化处理', parent=parent)
        self._kind = 0

    def __call__(self, img):
        if self._kind == 0:
            # python实现
            img = sobel_filter(img)
            # cv2实现
            # img = cv2_sobel(img)
        elif self._kind == 1:
            img = robert(img)
            # cv2实现
            # img = cv2_robert(img)
        elif self._kind == 2:
            img = prewitt_filter(img)
        elif self._kind == 3:
            img = laplacian_filter(img)
        return img

class AddNoiseItem(MyItem):
    def __init__(self, parent=None):
        super().__init__('加性噪声', parent=parent)
        self._kind = 0
        self._scale = 0.1

    def __call__(self, img):
        if self._kind == 0:
            img = gasuss_noise(img,self._scale)
        elif self._kind == 1:
            img = rayleigh_noise(img,self._scale)
        elif self._kind == 2:
            img = gamma_noise(img,self._scale)
        elif self._kind == 3:
            img = uniform_noise(img,self._scale)
        elif self._kind == 4:
            img = impluse_noise(img,self._scale)
        elif self._kind == 5:
            img = exponential_noise(img,self._scale)
        return img

class FrequencyFilterItem(MyItem):
    def __init__(self, parent=None):
        super().__init__('频域滤波', parent=parent)
        self._kind = 0
        self._scale = 30
        self._n = 1
    def __call__(self, img):
        if self._kind == 0 or self._kind == 3:
            img = idealFilter(img,self._scale,self._kind)
        elif self._kind == 1 or self._kind == 4:
            img = butterworthFilter(img,self._scale,self._n,self._kind)
        elif self._kind == 2 or self._kind == 5:
            img = GaussianFilter(img,self._scale,self._kind)
        return img


class SelectFilterItem(MyItem):
    def __init__(self, parent=None):
        super().__init__('选择滤波', parent=parent)
        self._kind = 0
        self._scale = 30
        self._n = 1
        self._W = 10
    def __call__(self, img):
        if self._kind == 0 or self._kind == 3:
            img = idealSelectFilter(img,self._scale,self._W,self._kind)
        elif self._kind == 1 or self._kind == 4:
            img = butterworthSelectFilter(img,self._scale,self._n,self._W,self._kind)
        elif self._kind == 2 or self._kind == 5:
            img = GaussianSelectFilter(img,self._scale,self._W,self._kind)
        elif self._kind == 6 or self._kind == 7:
            img = idealNotchFilter(img,self._scale,self._kind)
        return img

class ColorImageProcessItem(MyItem):
    def __init__(self, parent=None):
        super().__init__('彩色图像处理', parent=parent)
        self._kind = 0
        self._H = 100
        self._S = 100
        self._V = 100
        self._color_kind = 0

    def __call__(self, img):
        if self._kind == 0:
            img = hsvProcess(img,self._H,self._S,self._V)
        elif self._kind == 1:
            img = rgb2cmy(img,self._H,self._S,self._V)
        elif self._kind == 2:
            img = rgb2hsi(img,self._H,self._S,self._V)
        elif self._kind == 3:
            img = pseudoColorTrans(img,self._H,self._S,self._V,self._color_kind)
        return img


class IdCardPicGenerateItem(MyItem):
    def __init__(self, parent=None):
        super().__init__('证件照生成', parent=parent)
        self._kind = 0
        self._H = 100
        self._S = 100
        self._V = 100
    def __call__(self, img):
        img = idCardPicGenerate(img, self._kind)
        return img