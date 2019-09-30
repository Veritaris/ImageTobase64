# from fbs_runtime.application_context.PyQt5 import ApplicationContext
from GUI import interface
from GUI.frameless import FramelessWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets, QtCore
import sys
import base64
from PyQt5.QtGui import QPixmap, QImage

# self.graphicsScene = QtWidgets.QGraphicsScene(self.selectWidget)
# self.graphicsView = QtWidgets.QGraphicsView(self.graphicsScene)

colorsDict = {
    "white": "rgb(255, 255, 255)",
    "lavender": "rgb(158, 109, 207)",
    "lightLavender": "rgb(179, 147, 210)",
    "bgGrey": "rgb(53, 53, 53)",
    "buttonGrey": "rgb(63, 63, 63)",
    "widgetGrey": "rgb(68, 68, 68)",
    "errorRed": "rgb(200, 16, 16)",
    "okLabelGreen": "rgb(0, 200, 83);",
    "warnLabelYellow": "rgb(255, 196, 0);",
    "denyLabelRed": "rgb(229, 57, 53);"
}


class MainWindow(QtWidgets.QMainWindow, interface.Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.chooseFileButton.clicked.connect(self.select_file)
        self.saveConvertedFileButton.clicked.connect(self.save_file)

        self.filePathLine.setStyleSheet(
            f"""
            #filePathLine {{
                font-family:AlegreyaSans-Thin; 
                font-size: 12px;
                border-radius: 5px;
                border: 1px solid grey;
                color: {colorsDict["white"]};
                background-color: {colorsDict["buttonGrey"]};
            }}
            """
        )

        self.convertedImage.setStyleSheet(
            f"""
            #convertedImage {{
                font-family:AlegreyaSans-Thin; 
                font-size: 12px;
                border-radius: 5px;
                border: 1px solid grey;
                color: {colorsDict["white"]};
                background-color: {colorsDict["buttonGrey"]};
            }}
            #convertedImage:flat {{ border:none; }}
            """
        )



        self.convertFileButton.setStyleSheet(
            f"""
             #convertFileButton {{ 
                font-family:AlegreyaSans-Thin; 
                font-size: 12px;
                margin-left: 6px;
                margin-right: 6px;
            }}
             #convertFileButton:flat {{ border: none; }}
             #convertFileButton {{
                 color: {colorsDict["white"]};
                 background-color: {colorsDict["buttonGrey"]};
                 border-radius: 2px;
             }}
             #convertFileButton:pressed {{
                 background-color: {colorsDict["lavender"]};
             }}
             """
        )

        self.saveConvertedFileButton.setStyleSheet(
            f"""
             #saveConvertedFileButton {{ 
                font-family:AlegreyaSans-Thin; 
                font-size: 12px;
                margin-left: 6px;
                margin-right: 6px;
            }}
             #saveConvertedFileButton:flat {{ border: none; }}
             #saveConvertedFileButton {{
                 color: {colorsDict["white"]};
                 background-color: {colorsDict["buttonGrey"]};
                 border-radius: 2px;
             }}
             #saveConvertedFileButton:pressed {{
                 background-color: {colorsDict["lavender"]};
             }}
             """
        )

        self.chooseFileButton.setStyleSheet(
            f"""
             #chooseFileButton {{ 
                font-family:AlegreyaSans-Thin; 
                font-size: 12px;
            }}
             #chooseFileButton:flat {{ border: none; }}
             #chooseFileButton {{
                 color: {colorsDict["white"]};
                 background-color: {colorsDict["buttonGrey"]};
                 border-radius: 2px;
             }}
             #chooseFileButton:pressed {{
                 background-color: {colorsDict["lavender"]};
             }}
             """
        )

    def select_file(self):
        self.parseFileNames = QFileDialog.getOpenFileNames()[0]
        self.filePath = self.parseFileNames[0]
        self.filePathLine.setText(self.filePath)
        self.graphicsScene.clear()
        self.preview_img = QImage(self.filePath)
        self.pix_map = QPixmap.fromImage(self.preview_img)
        self.graphicsScene.addPixmap(self.pix_map)
        self.graphicsView.fitInView(QtCore.QRectF(0, 0, self.preview_img.size().height(), self.preview_img.size().width()),QtCore.Qt.KeepAspectRatio)
        self.graphicsScene.update()
        self.convert_image()

    def save_file(self):
        with open(self.filePath.split(".")[0] + "_base64.txt", "w") as f:
            f.write(self.data)


    def convert_image(self):
        with open(self.filePath, "rb") as f:
            self.data = base64.b64encode(f.read()).decode("utf-8")
            self.convertedImage.setText(self.data)


def __run__(window_object):
    from PyQt5.QtWidgets import QApplication

    # appctxt = ApplicationContext()

    app = QApplication(sys.argv)

    app.setStyleSheet(
        f"""
        QToolTip {{
            background-color: yellow;
        }}
        QMainWindow {{ 
             font-family:AlegreyaSans-Thin; 
             font-size: 12px;
         }}
        TitleBar {{
            background-color: {colorsDict["lavender"]};
        }}
        #buttonMinimum, #buttonClose {{
            color: {colorsDict['white']};
            border: none;
            background-color: {colorsDict["lavender"]};
        }}
        #buttonMinimum:hover {{
            color: {colorsDict['white']};
            background-color: {colorsDict["lavender"]};
        }}
        #buttonClose:hover {{
            color: {colorsDict['white']};
            background-color: {colorsDict["lavender"]};
        }}
        #buttonMinimum:pressed {{
            color: {colorsDict['white']};
            background-color: {colorsDict["lavender"]};
        }}
        #buttonClose:pressed {{
            color: {colorsDict['white']};
            background-color: {colorsDict["lavender"]};
        }}
        """
    )
    mainWindowTopBar = FramelessWindow()
    mainWindowBody = window_object()
    mainWindowBody.setFixedSize(mainWindowBody.size())
    mainWindowTopBar.setWidget(mainWindowBody)

    # window center alignment
    centerPoint = QtWidgets.QDesktopWidget().availableGeometry().center()
    halfWindowSize = QtCore.QPoint(750 / 2, (250 + 38) / 2)
    mainWindowTopBar.move(centerPoint - halfWindowSize)

    mainWindowTopBar.show()


    sys.exit(app.exec_())
    # exit_code = appctxt.app.exec_()
    # sys.exit(exit_code)


__run__(MainWindow)

