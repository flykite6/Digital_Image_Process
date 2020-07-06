from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidget, QAbstractItemView, QHeaderView, QSpinBox, QDoubleSpinBox, QCheckBox, \
    QComboBox, QWidget, QTableWidgetItem, QSlider, QLabel


class TableWidget(QTableWidget):
    def __init__(self, parent=None):
        super(TableWidget, self).__init__(parent=parent)
        self.mainwindow = parent
        self.setShowGrid(True)  # 显示网格
        self.setAlternatingRowColors(True)  # 隔行显示颜色
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().sectionResizeMode(QHeaderView.Stretch)
        self.verticalHeader().sectionResizeMode(QHeaderView.Stretch)
        self.horizontalHeader().setStretchLastSection(True)
        self.setFocusPolicy(Qt.NoFocus)

    def signal_connect(self):
        for spinbox in self.findChildren(QSpinBox):
            spinbox.valueChanged.connect(self.update_item)
        for doublespinbox in self.findChildren(QDoubleSpinBox):
            doublespinbox.valueChanged.connect(self.update_item)
        for combox in self.findChildren(QComboBox):
            combox.currentIndexChanged.connect(self.update_item)
        for checkbox in self.findChildren(QCheckBox):
            checkbox.stateChanged.connect(self.update_item)
        for qslider in self.findChildren(QSlider):
            qslider.valueChanged.connect(self.update_item)

    def update_item(self):
        param = self.get_params()
        self.mainwindow.useListWidget.currentItem().update_params(param)
        self.mainwindow.update_image()

    def update_params(self, param=None):
        for key in param.keys():
            box = self.findChild(QWidget, name=key)
            if isinstance(box, QSpinBox) or isinstance(box, QDoubleSpinBox):
                box.setValue(param[key])
            elif isinstance(box, QComboBox):
                box.setCurrentIndex(param[key])
            elif isinstance(box, QCheckBox):
                box.setChecked(param[key])
            elif isinstance(box, QSlider):
                box.setValue(param[key])

    def get_params(self):
        param = {}
        for spinbox in self.findChildren(QSpinBox):
            param[spinbox.objectName()] = spinbox.value()
        for doublespinbox in self.findChildren(QDoubleSpinBox):
            param[doublespinbox.objectName()] = doublespinbox.value()
        for combox in self.findChildren(QComboBox):
            param[combox.objectName()] = combox.currentIndex()
        for combox in self.findChildren(QCheckBox):
            param[combox.objectName()] = combox.isChecked()
        for qslider in self.findChildren(QSlider):
            param[qslider.objectName()] = qslider.value()
        return param


class GeometricTransTableWight(TableWidget):
    def __init__(self, parent=None):
        super(GeometricTransTableWight, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['放大|缩小','图像镜像','图像旋转','图像裁剪'])
        self.kind_comBox.setObjectName('kind')

        self.setColumnCount(2)
        self.setRowCount(2)


        # self.rate_value_doubleBox = QDoubleSpinBox()
        # self.rate_value_doubleBox.setObjectName('rate')
        # self.rate_value_doubleBox.setDecimals(1)
        # self.rate_value_spinBox.setMinimum()
        # self.rate_value_doubleBox.setSingleStep(0.1)
        self.rate_value_spinBox = QSpinBox()
        self.rate_value_spinBox.setObjectName('rate')
        self.rate_value_spinBox.setRange(0,360)
        self.rate_value_spinBox.setSingleStep(10)
        # self.rate_value_spinBox.setSuffix("%")
        self.setItem(0, 0, QTableWidgetItem('类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('比例%|角度°'))
        self.setCellWidget(1, 1, self.rate_value_spinBox)
        self.signal_connect()

class GrayingTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(GrayingTableWidget, self).__init__(parent=parent)

        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['灰度化', '图像反转', '二值化','幂律变换'])
        self.kind_comBox.setObjectName('kind')

        self.c_value_spinBox = QSpinBox()
        self.c_value_spinBox.setObjectName('c_value')
        self.c_value_spinBox.setMinimum(1)
        self.c_value_spinBox.setSingleStep(1)

        self.γ_value_spinBox = QSpinBox()
        self.γ_value_spinBox.setObjectName('γ_value')
        self.γ_value_spinBox.setMinimum(1)
        self.γ_value_spinBox.setSingleStep(1)

        self.setColumnCount(2)
        self.setRowCount(3)
        self.setItem(0, 0, QTableWidgetItem('类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('c值(幂律变换)'))
        self.setCellWidget(1, 1, self.c_value_spinBox)
        self.setItem(2, 0, QTableWidgetItem('γ值(幂律变换)'))
        self.setCellWidget(2, 1, self.γ_value_spinBox)

        self.signal_connect()

class EqualizeTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(EqualizeTableWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['直方图均衡化', '直方图匹配'])
        self.kind_comBox.setObjectName('kind')
        self.setColumnCount(2)
        self.setRowCount(1)
        self.setItem(0, 0, QTableWidgetItem('类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.signal_connect()


class FilterTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(FilterTabledWidget, self).__init__(parent=parent)

        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['均值滤波', '中值滤波','高斯滤波'])
        self.kind_comBox.setObjectName('kind')


        self.ksize_spinBox = QSpinBox()
        self.ksize_spinBox.setObjectName('ksize')
        self.ksize_spinBox.setMinimum(1)
        self.ksize_spinBox.setSingleStep(2)

        self.sigma_DoubleBox = QDoubleSpinBox()
        self.sigma_DoubleBox.setObjectName('sigma')
        self.sigma_DoubleBox.setMinimum(1)
        self.sigma_DoubleBox.setSingleStep(1)

        self.setColumnCount(2)
        self.setRowCount(3)
        self.setItem(0, 0, QTableWidgetItem('类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('size'))
        self.setCellWidget(1, 1, self.ksize_spinBox)
        self.setItem(2, 0, QTableWidgetItem('sigma(高斯滤波)'))
        self.setCellWidget(2, 1, self.sigma_DoubleBox)

        self.signal_connect()


class SharpenItemTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(SharpenItemTableWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['sobel算子','robert算子','prewitt算子','laplacian算子'])
        self.kind_comBox.setObjectName('kind')

        self.setColumnCount(2)
        self.setRowCount(1)
        self.setItem(0, 0, QTableWidgetItem('类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.signal_connect()

class AddNoiseItemTableWidget(TableWidget):
    def __init__(self, parent=None):
        super(AddNoiseItemTableWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['高斯噪声','瑞利噪声','伽马噪声','均匀噪声','椒盐噪声','指数噪声'])
        self.kind_comBox.setObjectName('kind')

        self.ksize_DoubleBox = QDoubleSpinBox()
        self.ksize_DoubleBox.setMinimum(0)
        self.ksize_DoubleBox.setSingleStep(0.1)
        self.ksize_DoubleBox.setObjectName('scale')

        self.setColumnCount(2)
        self.setRowCount(2)
        self.setItem(0, 0, QTableWidgetItem('噪声类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('噪声比例'))
        self.setCellWidget(1, 1, self.ksize_DoubleBox)
        self.signal_connect()


class FrequencyFilterTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(FrequencyFilterTabledWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['理想低通滤波','巴特沃思低通滤波','高斯低通滤波','理想高通滤波','巴特沃思高通滤波','高斯高通滤波'])
        self.kind_comBox.setObjectName('kind')
        self.ksize_SpinBox = QSpinBox()
        self.ksize_SpinBox.setMinimum(10)
        self.ksize_SpinBox.setSingleStep(10)
        self.ksize_SpinBox.setObjectName('scale')
        self.n_Spinbox = QSpinBox()
        self.n_Spinbox.setMinimum(1)
        self.n_Spinbox.setSingleStep(1)
        self.n_Spinbox.setObjectName('n')

        self.setColumnCount(2)
        self.setRowCount(3)
        self.setItem(0, 0, QTableWidgetItem('滤波类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('半径r'))
        self.setCellWidget(1, 1, self.ksize_SpinBox)
        self.setItem(2,0,QTableWidgetItem('阶数n'))
        self.setCellWidget(2,1,self.n_Spinbox)
        self.signal_connect()


class SelectFilterTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(SelectFilterTabledWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['理想带阻滤波', '巴特沃思带阻滤波', '高斯带阻滤波', '理想带通滤波', '巴特沃思带通滤波', '高斯带通滤波','理想带阻陷波','理想带通陷波'])
        self.kind_comBox.setObjectName('kind')
        self.ksize_SpinBox = QSpinBox()
        self.ksize_SpinBox.setMinimum(0)
        self.ksize_SpinBox.setMaximum(300)
        self.ksize_SpinBox.setSingleStep(10)
        self.ksize_SpinBox.setObjectName('scale')
        self.W_Spinbox = QSpinBox()
        self.W_Spinbox.setMinimum(0)
        self.W_Spinbox.setMaximum(500)
        self.W_Spinbox.setSingleStep(10)
        self.W_Spinbox.setObjectName('W')
        self.n_Spinbox = QSpinBox()
        self.n_Spinbox.setMinimum(1)
        self.n_Spinbox.setSingleStep(1)
        self.n_Spinbox.setObjectName('n')

        self.setColumnCount(2)
        self.setRowCount(4)
        self.setItem(0, 0, QTableWidgetItem('滤波类型'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('半径r'))
        self.setCellWidget(1, 1, self.ksize_SpinBox)
        self.setItem(2, 0, QTableWidgetItem('带宽W'))
        self.setCellWidget(2, 1, self.W_Spinbox)
        self.setItem(3, 0, QTableWidgetItem('阶数n'))
        self.setCellWidget(3, 1, self.n_Spinbox)
        self.signal_connect()

class ColorImageProcessTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(ColorImageProcessTabledWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['RGB模型', 'CMY模型','HSI模型','伪彩色变换'])
        # self.kind_comBox.addItems(['彩色模型', '伪彩色变换', '真彩色变换'])
        self.kind_comBox.setObjectName('kind')

        # self.H_qslider = QSlider(Qt.Horizontal)
        self.H_qslider = MyQSlider()
        self.H_qslider.setOrientation(Qt.Horizontal)
        self.H_qslider.setMinimum(0)
        self.H_qslider.setMaximum(150)
        self.H_qslider.setSingleStep(10)
        self.H_qslider.setTickPosition(QSlider.TicksBelow)
        self.H_qslider.setTickInterval(10)
        self.H_qslider.setObjectName('H')

        # self.S_qslider = QSlider(Qt.Horizontal)
        self.S_qslider = MyQSlider()
        self.S_qslider.setOrientation(Qt.Horizontal)
        self.S_qslider.setMinimum(0)
        self.S_qslider.setMaximum(150)
        self.S_qslider.setSingleStep(10)
        self.S_qslider.setTickPosition(QSlider.TicksBelow)
        self.S_qslider.setTickInterval(10)
        self.S_qslider.setObjectName('S')

        # self.V_qslider = QSlider(Qt.Horizontal)
        self.V_qslider = MyQSlider()
        self.V_qslider.setOrientation(Qt.Horizontal)
        self.V_qslider.setMinimum(0)
        self.V_qslider.setMaximum(150)
        self.V_qslider.setSingleStep(10)
        self.V_qslider.setTickPosition(QSlider.TicksBelow)
        self.V_qslider.setTickInterval(10)
        self.V_qslider.setObjectName('V')

        self.pseudoColor_comBox = QComboBox()
        self.pseudoColor_comBox.addItems(['COLORMAP_AUTUMN', 'COLORMAP_BONE', 'COLORMAP_JET', 'COLORMAP_WINTER', 'COLORMAP_RAINBOW','COLORMAP_OCEAN','COLORMAP_SUMMER','COLORMAP_SPRING','COLORMAP_COOL','COLORMAP_HSV','COLORMAP_PINK','COLORMAP_HOT'])
        # self.kind_comBox.addItems(['彩色模型', '伪彩色变换', '真彩色变换'])
        self.pseudoColor_comBox.setObjectName('color_kind')


        self.setColumnCount(2)
        self.setRowCount(5)
        self.setItem(0, 0, QTableWidgetItem('颜色变换'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.setItem(1, 0, QTableWidgetItem('B通道'))
        self.setCellWidget(1, 1, self.H_qslider)
        self.setItem(2, 0, QTableWidgetItem('G通道'))
        self.setCellWidget(2, 1, self.S_qslider)
        self.setItem(3, 0, QTableWidgetItem('R通道'))
        self.setCellWidget(3, 1, self.V_qslider)
        self.setItem(4, 0, QTableWidgetItem('伪彩色类型'))
        self.setCellWidget(4, 1, self.pseudoColor_comBox)

        self.signal_connect()


class IdCardPicGenerateTabledWidget(TableWidget):
    def __init__(self, parent=None):
        super(IdCardPicGenerateTabledWidget, self).__init__(parent=parent)
        self.kind_comBox = QComboBox()
        self.kind_comBox.addItems(['蓝底', '红底','白底'])
        self.kind_comBox.setObjectName('kind')
        self.setColumnCount(2)
        self.setRowCount(1)
        self.setItem(0, 0, QTableWidgetItem('证件照合成'))
        self.setCellWidget(0, 1, self.kind_comBox)
        self.signal_connect()

class MyQSlider(QSlider):
    def __init__(self,parent=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        label = QLabel(self)
        self.label = label
        label.setText('100')
        label.setStyleSheet('background-color:cyan;color:red')
        label.hide()

    def mousePressEvent(self, evt):
        super().mousePressEvent(evt)
        y = (1-((self.value()-self.minimum())/(self.maximum()-self.minimum())))*(self.height()-self.label.height())
        x =  (self.width()-self.label.width())/2
        self.label.move(x,y)
        self.label.show()
        self.label.setText(str(self.value()))

    def mouseMoveEvent(self, evt):
        super().mouseMoveEvent(evt)
        y = (1-((self.value()-self.minimum())/(self.maximum()-self.minimum())))*(self.height()-self.label.height())
        x =  (self.width()-self.label.width())/2
        self.label.move(x,y)
        self.label.setText(str(self.value()))
        self.label.adjustSize()

    def mouseReleaseEvent(self, evt):
        super().mouseReleaseEvent(evt)
        self.label.hide()
