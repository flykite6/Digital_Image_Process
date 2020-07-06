import sys
from cv2 import cvtColor,calcHist,imread,COLOR_GRAY2BGR
import matplotlib.pyplot as plt
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, QMainWindow, QApplication, QDockWidget, QLabel

from custom.stackedWidget import StackedWidget
from custom.treeView import FileSystemTreeView
from custom.listWidgets import FuncListWidget, UsedListWidget
from custom.graphicsView import GraphicsView
from function.GeometricTrans.Ratate import ratate


class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        QApplication.processEvents()
        self.childArea = childWindow()
        self.tool_bar = self.addToolBar('工具栏')
        self.action_right_rotate = QAction(QIcon("icons/右旋转.png"), "向右旋转90", self)
        self.action_left_rotate = QAction(QIcon("icons/左旋转.png"), "向左旋转90°", self)
        self.action_histogram = QAction(QIcon("icons/直方图.png"), "直方图", self)
        self.action_right_rotate.triggered.connect(self.right_rotate)
        self.action_left_rotate.triggered.connect(self.left_rotate)
        self.action_histogram.triggered.connect(self.histogram)
        # 将上述动作关联到某一个菜单项里面
        self.tool_bar.addActions((self.action_left_rotate, self.action_right_rotate, self.action_histogram))

        self.useListWidget = UsedListWidget(self)
        self.funcListWidget = FuncListWidget(self)
        self.stackedWidget = StackedWidget(self)
        self.fileSystemTreeView = FileSystemTreeView(self)
        self.graphicsView = GraphicsView(self)

        self.dock_file = QDockWidget(self)
        self.dock_file.setWidget(self.fileSystemTreeView)
        self.dock_file.setTitleBarWidget(QLabel('目录'))
        self.dock_file.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_func = QDockWidget(self)
        self.dock_func.setWidget(self.funcListWidget)
        self.dock_func.setTitleBarWidget(QLabel('图像操作'))
        self.dock_func.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_used = QDockWidget(self)
        self.dock_used.setWidget(self.useListWidget)
        self.dock_used.setTitleBarWidget(QLabel('已选操作'))
        self.dock_used.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_used.setFeatures(QDockWidget.NoDockWidgetFeatures)

        self.dock_attr = QDockWidget(self)
        self.dock_attr.setWidget(self.stackedWidget)
        self.dock_attr.setTitleBarWidget(QLabel('属性'))
        self.dock_attr.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dock_attr.close()

        self.setCentralWidget(self.graphicsView)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock_file)
        self.dock_file.setMinimumWidth(400)
        self.dock_file.showMinimized()
        self.addDockWidget(Qt.TopDockWidgetArea, self.dock_func)
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_used)
        self.dock_used.setMinimumWidth(400)
        self.dock_used.showMinimized()
        self.addDockWidget(Qt.RightDockWidgetArea, self.dock_attr)
        self.dock_attr.setMinimumHeight(500)

        self.setWindowTitle('数字图像处理')
        self.setWindowIcon(QIcon('icons/main.png'))
        self.src_img = None
        self.cur_img = None

    def update_image(self):
        if self.src_img is None:
            return
        img = self.process_image()
        self.cur_img = img
        self.graphicsView.update_image(img)

    def change_image(self, img):
        self.src_img = img
        img = self.process_image()
        self.cur_img = img
        self.graphicsView.change_image(img)

    def process_image(self):
        img = self.src_img.copy()
        for i in range(self.useListWidget.count()):
            img = self.useListWidget.item(i)(img)
        return img

    def right_rotate(self):
        self.cur_img = ratate(self.cur_img,90)
        self.graphicsView.rotate(90)

    def left_rotate(self):
        self.cur_img = ratate(self.cur_img, -90)
        self.graphicsView.rotate(-90)

    def histogram(self):
        color = ('b', 'g', 'r')
        img = self.cur_img
        shape = img.shape
        if len(shape) != 3:
            img = cvtColor(self.cur_img,COLOR_GRAY2BGR)
        for i, col in enumerate(color):
            histr = calcHist([img], [i], None, [256], [0, 256])
            histr = histr.flatten()
            plt.plot(range(256), histr, color=col)
            plt.xlim([0, 256])
        plt.savefig('histogram.png')
        plt.close()
        self.img = imread('./histogram.png')
        self.childArea.display(self.img)
        self.childArea.show()


class childWindow(QMainWindow):
    def __init__(self,parent=None):
        super(childWindow, self).__init__(parent)
        self.setWindowTitle('图像的直方图')
        self.graphicsView1 = GraphicsView(self)
        self.setCentralWidget(self.graphicsView1)
    def display(self,img):
        self.graphicsView1.change_image(img)






if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(open('styleSheet.qss', encoding='utf-8').read())
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
