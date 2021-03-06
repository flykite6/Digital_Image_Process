###                                                    数字图像处理系统

#### 软件界面

![interface Image](https://github.com/flykite6/Digital_Image_Process/raw/master/images/界面.png)

备注：界面代码参考自https://github.com/JiageWang/opencv-pyqt5

### 系统功能

* 几何变换
  * 图像放大|缩小
  * 图像镜像
  * 图像旋转
  * 图像裁剪
* 灰度变换
  * 图像灰度化
  * 图像反转
  * 图像二值化
  * 幂律变换
* 直方图处理
  * 直方图均衡化
  * 直方图匹配
* 平滑处理
  * 均值滤波
  * 中值滤波
  * 高斯滤波
* 锐化处理
  * sobel算子
  * robert算子
  * prewitt算子
  * laplacian算子
* 加性噪声
  * 高斯噪声
  * 瑞利噪声
  * 伽马噪声
  * 均匀噪声
  * 椒盐噪声
  * 指数噪声
* 频域滤波
  * 理想低通|高通滤波
  * 巴特沃斯低通|高通滤波
  * 高斯低通|高通滤波
  * 理想带阻|带通滤波
  * 巴特沃斯带阻|带通滤波
  * 高斯带阻|带通滤波
  * 理想带阻|带通陷波滤波
* 彩色图像处理
  * RGB转CMY
  * RGB转HSI
  * RGB各个成分的调节
  * 伪彩色图像生成
* 证件照生成



### 运行环境

- python-opencv4.2
- pyqt5
- matplotlib3.2.1
- numpy1.18.4
- dlib



### 使用说明

> 配置好相关环境，直接运行main.py就ok