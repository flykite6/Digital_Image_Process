from cv2 import selectROI,imwrite
from PyQt5.QtWidgets import QMainWindow, QFileDialog


class childwindow1(QMainWindow):
    def __init__(self,parent=None):
        super(childwindow1, self).__init__(parent)
    def openfile(self):
        fname, _  = QFileDialog.getOpenFileName(self, 'Open file', '.', 'Image Files(*.jpg *.bmp *.png *.jpeg *.rgb *.tif)')
        return fname
    def selectROI(self,img):
        bbox = selectROI(img, False)
        cut = img[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
        imwrite('cut.jpg', cut)

