from os import system
from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog,QStackedWidget,QFileDialog,QMessageBox
from PIL import Image,ImageOps
import sys

class main(QDialog):
      def __init__(self):
            super(main, self).__init__()
            loadUi('src/main1.ui', self)
            self.selectFile.clicked.connect(self.selectFile_clicked)
      def selectFile_clicked(self):
            file = QFileDialog.getOpenFileName(self, 'Select a folder:','All Files (*);;Images (*.png *.xpm *.jpg)')
            img = Image.open(file[0])
            grayed = ImageOps.grayscale(img)
            grayed.show()
            add = saveScreen(grayed,img.format,file[0])
            widget.addWidget(add)   
            widget.setCurrentIndex(widget.currentIndex()+1)
class saveScreen(QDialog):
      file_name = "unnamed.png"
      IMG = None
      Format = None
      Path = ''
      def __init__(self,img,format,originalPath):
            super(saveScreen,self).__init__()
            loadUi('src/savescreen.ui',self)
            self.No.clicked.connect(self.NO)
            self.Yes.clicked.connect(self.YES)
            self.savePath.clicked.connect(self.changeSaveLocation)
            self.IMG = img
            self.Format = format
            self.Path = originalPath
      def changeSaveLocation(self):
            self.Path = QFileDialog.getExistingDirectory(self)
            self.Path+='/'
            print(self.Path)
      def NO(self):
            self.close()
      def YES(self):
            FormatToExtensio = {'PNG':'.png','JPG':'.jpg','JPEG':'.jpeg'}
            self.file_name = self.fileName.text()
            system('cd '+self.Path+'/')
            res = self.Path+self.file_name+FormatToExtensio[self.Format]
            print(res)
            self.IMG.save(res,format=self.Format)
            saved = QMessageBox()
            saved.setWindowTitle("Image Saved")
            saved.setText("Image Saved")
            saved.exec()
            self.close()
            app.closeAllWindows()



      
app =  QtWidgets.QApplication([])
widget = QStackedWidget()
Screen = main()
widget.addWidget(Screen)
widget.setBaseSize(Screen.width(),Screen.height())
widget.setMinimumSize(Screen.width(),Screen.height())
widget.setFixedHeight(Screen.height())
widget.setFixedWidth(Screen.width())
widget.show()
sys.exit(app.exec_())