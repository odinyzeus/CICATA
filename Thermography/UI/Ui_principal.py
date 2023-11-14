# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'principal.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QDoubleSpinBox,
    QFormLayout, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QProgressBar, QPushButton, QRadioButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget
import UI.resources.Thermography_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.ApplicationModal)
        MainWindow.resize(975, 725)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionOpen.setCheckable(True)
        icon = QIcon()
        iconThemeName = u"system-file-manager"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionOpen.setIcon(icon)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon1 = QIcon()
        iconThemeName = u"document-save"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionSave.setIcon(icon1)
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        icon2 = QIcon()
        iconThemeName = u"application-exit"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.actionExit.setIcon(icon2)
        self.actionExecute = QAction(MainWindow)
        self.actionExecute.setObjectName(u"actionExecute")
        self.actionImage_Generation = QAction(MainWindow)
        self.actionImage_Generation.setObjectName(u"actionImage_Generation")
        self.actionLockIn = QAction(MainWindow)
        self.actionLockIn.setObjectName(u"actionLockIn")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.Cabecera = QFrame(self.centralwidget)
        self.Cabecera.setObjectName(u"Cabecera")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.Cabecera.sizePolicy().hasHeightForWidth())
        self.Cabecera.setSizePolicy(sizePolicy1)
        self.Cabecera.setMinimumSize(QSize(0, 150))
        self.Cabecera.setMaximumSize(QSize(16777215, 150))
        self.Cabecera.setBaseSize(QSize(0, 150))
        self.Cabecera.setFrameShape(QFrame.Box)
        self.Cabecera.setFrameShadow(QFrame.Raised)
        self.Cabecera.setLineWidth(2)
        self.horizontalLayout = QHBoxLayout(self.Cabecera)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.LogoCicata = QLabel(self.Cabecera)
        self.LogoCicata.setObjectName(u"LogoCicata")
        self.LogoCicata.setMinimumSize(QSize(120, 120))
        self.LogoCicata.setMaximumSize(QSize(120, 150))
        self.LogoCicata.setFrameShape(QFrame.Box)
        self.LogoCicata.setFrameShadow(QFrame.Raised)
        self.LogoCicata.setLineWidth(2)
        self.LogoCicata.setPixmap(QPixmap(u":/Header/IPN_CICATA.png"))
        self.LogoCicata.setScaledContents(True)

        self.horizontalLayout.addWidget(self.LogoCicata)

        self.label = QLabel(self.Cabecera)
        self.label.setObjectName(u"label")
        self.label.setFrameShape(QFrame.Box)
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setLineWidth(2)
        self.label.setTextFormat(Qt.RichText)

        self.horizontalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.Cabecera)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setMinimumSize(QSize(120, 120))
        self.label_2.setMaximumSize(QSize(120, 150))
        self.label_2.setBaseSize(QSize(120, 120))
        self.label_2.setFrameShape(QFrame.Box)
        self.label_2.setFrameShadow(QFrame.Raised)
        self.label_2.setLineWidth(2)
        self.label_2.setPixmap(QPixmap(u":/Header/LOGO POLI PANTONE 222 C.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 80)
        self.horizontalLayout.setStretch(2, 5)

        self.verticalLayout.addWidget(self.Cabecera)

        self.Cuerpo = QFrame(self.centralwidget)
        self.Cuerpo.setObjectName(u"Cuerpo")
        self.Cuerpo.setFrameShape(QFrame.Box)
        self.Cuerpo.setFrameShadow(QFrame.Raised)
        self.Cuerpo.setLineWidth(2)
        self.horizontalLayout_2 = QHBoxLayout(self.Cuerpo)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Parameters = QFrame(self.Cuerpo)
        self.Parameters.setObjectName(u"Parameters")
        self.Parameters.setFrameShape(QFrame.Box)
        self.Parameters.setFrameShadow(QFrame.Raised)
        self.Parameters.setLineWidth(2)
        self.verticalLayout_2 = QVBoxLayout(self.Parameters)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 5, 2, 5)
        self.parms_control = QFrame(self.Parameters)
        self.parms_control.setObjectName(u"parms_control")
        self.parms_control.setFrameShape(QFrame.StyledPanel)
        self.parms_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.parms_control)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.lblParameters = QLabel(self.parms_control)
        self.lblParameters.setObjectName(u"lblParameters")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lblParameters.sizePolicy().hasHeightForWidth())
        self.lblParameters.setSizePolicy(sizePolicy3)
        self.lblParameters.setFrameShape(QFrame.Box)
        self.lblParameters.setFrameShadow(QFrame.Raised)
        self.lblParameters.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.lblParameters)

        self.ctlProcess = QFrame(self.parms_control)
        self.ctlProcess.setObjectName(u"ctlProcess")
        self.ctlProcess.setFrameShape(QFrame.StyledPanel)
        self.ctlProcess.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.ctlProcess)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout.setHorizontalSpacing(5)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.initFrameLabel = QLabel(self.ctlProcess)
        self.initFrameLabel.setObjectName(u"initFrameLabel")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.initFrameLabel)

        self.initFrameSpinBox = QSpinBox(self.ctlProcess)
        self.initFrameSpinBox.setObjectName(u"initFrameSpinBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.initFrameSpinBox.sizePolicy().hasHeightForWidth())
        self.initFrameSpinBox.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.initFrameSpinBox)

        self.finalFrameLabel = QLabel(self.ctlProcess)
        self.finalFrameLabel.setObjectName(u"finalFrameLabel")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.finalFrameLabel)

        self.finalFrameSpinBox = QSpinBox(self.ctlProcess)
        self.finalFrameSpinBox.setObjectName(u"finalFrameSpinBox")
        sizePolicy4.setHeightForWidth(self.finalFrameSpinBox.sizePolicy().hasHeightForWidth())
        self.finalFrameSpinBox.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.finalFrameSpinBox)

        self.modulationLabel = QLabel(self.ctlProcess)
        self.modulationLabel.setObjectName(u"modulationLabel")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.modulationLabel)

        self.modulation = QDoubleSpinBox(self.ctlProcess)
        self.modulation.setObjectName(u"modulation")
        sizePolicy4.setHeightForWidth(self.modulation.sizePolicy().hasHeightForWidth())
        self.modulation.setSizePolicy(sizePolicy4)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.modulation)


        self.verticalLayout_3.addWidget(self.ctlProcess)


        self.verticalLayout_2.addWidget(self.parms_control)

        self.parms_info = QFrame(self.Parameters)
        self.parms_info.setObjectName(u"parms_info")
        self.parms_info.setFrameShape(QFrame.StyledPanel)
        self.parms_info.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.parms_info)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.lblInfo = QLabel(self.parms_info)
        self.lblInfo.setObjectName(u"lblInfo")
        sizePolicy3.setHeightForWidth(self.lblInfo.sizePolicy().hasHeightForWidth())
        self.lblInfo.setSizePolicy(sizePolicy3)
        self.lblInfo.setFrameShape(QFrame.Box)
        self.lblInfo.setFrameShadow(QFrame.Raised)
        self.lblInfo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lblInfo)

        self.info_data = QFrame(self.parms_info)
        self.info_data.setObjectName(u"info_data")
        self.info_data.setFrameShape(QFrame.StyledPanel)
        self.info_data.setFrameShadow(QFrame.Raised)
        self.formLayout_2 = QFormLayout(self.info_data)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(5)
        self.formLayout_2.setVerticalSpacing(5)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.framesLabel = QLabel(self.info_data)
        self.framesLabel.setObjectName(u"framesLabel")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.framesLabel)

        self.framesSpinBox = QSpinBox(self.info_data)
        self.framesSpinBox.setObjectName(u"framesSpinBox")
        sizePolicy4.setHeightForWidth(self.framesSpinBox.sizePolicy().hasHeightForWidth())
        self.framesSpinBox.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.framesSpinBox)

        self.frameRateLabel = QLabel(self.info_data)
        self.frameRateLabel.setObjectName(u"frameRateLabel")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.frameRateLabel)

        self.frameRate = QSpinBox(self.info_data)
        self.frameRate.setObjectName(u"frameRate")
        sizePolicy4.setHeightForWidth(self.frameRate.sizePolicy().hasHeightForWidth())
        self.frameRate.setSizePolicy(sizePolicy4)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.frameRate)

        self.heightLabel = QLabel(self.info_data)
        self.heightLabel.setObjectName(u"heightLabel")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.heightLabel)

        self.framesHeight = QSpinBox(self.info_data)
        self.framesHeight.setObjectName(u"framesHeight")
        sizePolicy4.setHeightForWidth(self.framesHeight.sizePolicy().hasHeightForWidth())
        self.framesHeight.setSizePolicy(sizePolicy4)
        self.framesHeight.setMaximum(4096)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.framesHeight)

        self.widthLabel = QLabel(self.info_data)
        self.widthLabel.setObjectName(u"widthLabel")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.widthLabel)

        self.frameWidth = QSpinBox(self.info_data)
        self.frameWidth.setObjectName(u"frameWidth")
        sizePolicy4.setHeightForWidth(self.frameWidth.sizePolicy().hasHeightForWidth())
        self.frameWidth.setSizePolicy(sizePolicy4)
        self.frameWidth.setMaximum(2048)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.frameWidth)

        self.durationLabel = QLabel(self.info_data)
        self.durationLabel.setObjectName(u"durationLabel")

        self.formLayout_2.setWidget(4, QFormLayout.LabelRole, self.durationLabel)

        self.duration = QLineEdit(self.info_data)
        self.duration.setObjectName(u"duration")

        self.formLayout_2.setWidget(4, QFormLayout.FieldRole, self.duration)


        self.verticalLayout_4.addWidget(self.info_data)


        self.verticalLayout_2.addWidget(self.parms_info)

        self.parms_method = QFrame(self.Parameters)
        self.parms_method.setObjectName(u"parms_method")
        self.parms_method.setFrameShape(QFrame.StyledPanel)
        self.parms_method.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.parms_method)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.lblInfo_2 = QLabel(self.parms_method)
        self.lblInfo_2.setObjectName(u"lblInfo_2")
        sizePolicy3.setHeightForWidth(self.lblInfo_2.sizePolicy().hasHeightForWidth())
        self.lblInfo_2.setSizePolicy(sizePolicy3)
        self.lblInfo_2.setFrameShape(QFrame.Box)
        self.lblInfo_2.setFrameShadow(QFrame.Raised)
        self.lblInfo_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lblInfo_2)

        self.frame = QFrame(self.parms_method)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.btnGeometry = QRadioButton(self.frame)
        self.btnGeometry.setObjectName(u"btnGeometry")

        self.verticalLayout_6.addWidget(self.btnGeometry)

        self.btnFourPoints = QRadioButton(self.frame)
        self.btnFourPoints.setObjectName(u"btnFourPoints")

        self.verticalLayout_6.addWidget(self.btnFourPoints)

        self.btnFourier = QRadioButton(self.frame)
        self.btnFourier.setObjectName(u"btnFourier")

        self.verticalLayout_6.addWidget(self.btnFourier)


        self.verticalLayout_5.addWidget(self.frame)


        self.verticalLayout_2.addWidget(self.parms_method)


        self.horizontalLayout_2.addWidget(self.Parameters)

        self.Process = QTabWidget(self.Cuerpo)
        self.Process.setObjectName(u"Process")
        self.tabVideo = QWidget()
        self.tabVideo.setObjectName(u"tabVideo")
        self.verticalLayout_8 = QVBoxLayout(self.tabVideo)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(2, 2, 2, 2)
        self.frame_10 = QFrame(self.tabVideo)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Box)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.frame_12.setLineWidth(2)
        self.verticalLayout_16 = QVBoxLayout(self.frame_12)
        self.verticalLayout_16.setSpacing(3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(3, 3, 3, 3)
        self.mediaPlayer = QVideoWidget(self.frame_12)
        self.mediaPlayer.setObjectName(u"mediaPlayer")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.mediaPlayer.sizePolicy().hasHeightForWidth())
        self.mediaPlayer.setSizePolicy(sizePolicy5)

        self.verticalLayout_16.addWidget(self.mediaPlayer)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Box)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.frame_11.setLineWidth(2)
        self.verticalLayout_15 = QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setSpacing(4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(2, 2, 2, 2)
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy6)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setFrameShadow(QFrame.Raised)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_4)

        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setContentsMargins(2, 2, -1, -1)

        self.verticalLayout_15.addLayout(self.formLayout_4)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.horizontalLayout_6.setStretch(0, 4)
        self.horizontalLayout_6.setStretch(1, 2)

        self.verticalLayout_8.addWidget(self.frame_10)

        self.play_control = QFrame(self.tabVideo)
        self.play_control.setObjectName(u"play_control")
        self.play_control.setFrameShape(QFrame.StyledPanel)
        self.play_control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.play_control)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.btnRew = QPushButton(self.play_control)
        self.btnRew.setObjectName(u"btnRew")
        self.btnRew.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnRew)

        self.btnStart = QPushButton(self.play_control)
        self.btnStart.setObjectName(u"btnStart")
        self.btnStart.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnStart)

        self.btnStop = QPushButton(self.play_control)
        self.btnStop.setObjectName(u"btnStop")
        self.btnStop.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnStop)

        self.btnFor = QPushButton(self.play_control)
        self.btnFor.setObjectName(u"btnFor")
        self.btnFor.setEnabled(False)

        self.horizontalLayout_3.addWidget(self.btnFor)

        self.videoSlider = QSlider(self.play_control)
        self.videoSlider.setObjectName(u"videoSlider")
        self.videoSlider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.videoSlider)


        self.verticalLayout_8.addWidget(self.play_control)

        self.verticalLayout_8.setStretch(0, 4)
        self.Process.addTab(self.tabVideo, "")
        self.tabProcessing = QWidget()
        self.tabProcessing.setObjectName(u"tabProcessing")
        self.verticalLayout_9 = QVBoxLayout(self.tabProcessing)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.Process_Phase = QTabWidget(self.tabProcessing)
        self.Process_Phase.setObjectName(u"Process_Phase")
        self.Process_Phase.setTabPosition(QTabWidget.West)
        self.get_images = QWidget()
        self.get_images.setObjectName(u"get_images")
        self.horizontalLayout_4 = QHBoxLayout(self.get_images)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.img_phase_1 = QFrame(self.get_images)
        self.img_phase_1.setObjectName(u"img_phase_1")
        self.img_phase_1.setFrameShape(QFrame.Box)
        self.img_phase_1.setFrameShadow(QFrame.Raised)
        self.img_phase_1.setLineWidth(2)
        self.gridLayout = QGridLayout(self.img_phase_1)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.img_p_1_1 = QLabel(self.img_phase_1)
        self.img_p_1_1.setObjectName(u"img_p_1_1")
        self.img_p_1_1.setFrameShape(QFrame.Box)
        self.img_p_1_1.setFrameShadow(QFrame.Raised)
        self.img_p_1_1.setLineWidth(2)

        self.gridLayout.addWidget(self.img_p_1_1, 0, 0, 1, 1)

        self.img_p_1_2 = QLabel(self.img_phase_1)
        self.img_p_1_2.setObjectName(u"img_p_1_2")
        self.img_p_1_2.setFrameShape(QFrame.Box)
        self.img_p_1_2.setFrameShadow(QFrame.Raised)
        self.img_p_1_2.setLineWidth(2)

        self.gridLayout.addWidget(self.img_p_1_2, 0, 1, 1, 1)

        self.img_p_1_3 = QLabel(self.img_phase_1)
        self.img_p_1_3.setObjectName(u"img_p_1_3")
        self.img_p_1_3.setFrameShape(QFrame.Box)
        self.img_p_1_3.setFrameShadow(QFrame.Raised)
        self.img_p_1_3.setLineWidth(2)

        self.gridLayout.addWidget(self.img_p_1_3, 1, 0, 1, 2)


        self.horizontalLayout_4.addWidget(self.img_phase_1)

        self.data_phase_1 = QFrame(self.get_images)
        self.data_phase_1.setObjectName(u"data_phase_1")
        self.data_phase_1.setFrameShape(QFrame.Box)
        self.data_phase_1.setFrameShadow(QFrame.Raised)
        self.data_phase_1.setLineWidth(2)
        self.verticalLayout_7 = QVBoxLayout(self.data_phase_1)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.data_phase_1)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy7)
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setLineWidth(2)
        self.formLayout_3 = QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.formLayout_3.setHorizontalSpacing(4)
        self.formLayout_3.setVerticalSpacing(4)
        self.formLayout_3.setContentsMargins(4, 4, 4, 4)
        self.heightLabel_2 = QLabel(self.frame_2)
        self.heightLabel_2.setObjectName(u"heightLabel_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.heightLabel_2)

        self.heightPhase = QSpinBox(self.frame_2)
        self.heightPhase.setObjectName(u"heightPhase")
        sizePolicy4.setHeightForWidth(self.heightPhase.sizePolicy().hasHeightForWidth())
        self.heightPhase.setSizePolicy(sizePolicy4)
        self.heightPhase.setMaximum(1080)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.heightPhase)

        self.widthLabel_2 = QLabel(self.frame_2)
        self.widthLabel_2.setObjectName(u"widthLabel_2")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.widthLabel_2)

        self.widthPhase = QSpinBox(self.frame_2)
        self.widthPhase.setObjectName(u"widthPhase")
        sizePolicy4.setHeightForWidth(self.widthPhase.sizePolicy().hasHeightForWidth())
        self.widthPhase.setSizePolicy(sizePolicy4)
        self.widthPhase.setMaximum(1080)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.widthPhase)

        self.framesToProcessLabel = QLabel(self.frame_2)
        self.framesToProcessLabel.setObjectName(u"framesToProcessLabel")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.framesToProcessLabel)

        self.framesToProcess = QSpinBox(self.frame_2)
        self.framesToProcess.setObjectName(u"framesToProcess")
        sizePolicy4.setHeightForWidth(self.framesToProcess.sizePolicy().hasHeightForWidth())
        self.framesToProcess.setSizePolicy(sizePolicy4)
        self.framesToProcess.setReadOnly(True)
        self.framesToProcess.setMaximum(100000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.framesToProcess)

        self.framesPerPeriodLabel = QLabel(self.frame_2)
        self.framesPerPeriodLabel.setObjectName(u"framesPerPeriodLabel")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.framesPerPeriodLabel)

        self.framesPerPeriod = QSpinBox(self.frame_2)
        self.framesPerPeriod.setObjectName(u"framesPerPeriod")
        sizePolicy4.setHeightForWidth(self.framesPerPeriod.sizePolicy().hasHeightForWidth())
        self.framesPerPeriod.setSizePolicy(sizePolicy4)
        self.framesPerPeriod.setReadOnly(True)
        self.framesPerPeriod.setMaximum(100000)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.framesPerPeriod)

        self.periodsLabel = QLabel(self.frame_2)
        self.periodsLabel.setObjectName(u"periodsLabel")

        self.formLayout_3.setWidget(4, QFormLayout.LabelRole, self.periodsLabel)

        self.periods = QSpinBox(self.frame_2)
        self.periods.setObjectName(u"periods")
        sizePolicy4.setHeightForWidth(self.periods.sizePolicy().hasHeightForWidth())
        self.periods.setSizePolicy(sizePolicy4)
        self.periods.setReadOnly(True)
        self.periods.setMaximum(100000)

        self.formLayout_3.setWidget(4, QFormLayout.FieldRole, self.periods)

        self.digital_frequencySpinBox = QSpinBox(self.frame_2)
        self.digital_frequencySpinBox.setObjectName(u"digital_frequencySpinBox")
        sizePolicy4.setHeightForWidth(self.digital_frequencySpinBox.sizePolicy().hasHeightForWidth())
        self.digital_frequencySpinBox.setSizePolicy(sizePolicy4)
        self.digital_frequencySpinBox.setMaximum(100000)

        self.formLayout_3.setWidget(5, QFormLayout.FieldRole, self.digital_frequencySpinBox)

        self.digital_frequencyLabel = QLabel(self.frame_2)
        self.digital_frequencyLabel.setObjectName(u"digital_frequencyLabel")
        self.digital_frequencyLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.formLayout_3.setWidget(5, QFormLayout.LabelRole, self.digital_frequencyLabel)

        self.wNLabel = QLabel(self.frame_2)
        self.wNLabel.setObjectName(u"wNLabel")

        self.formLayout_3.setWidget(6, QFormLayout.LabelRole, self.wNLabel)

        self.wNLineEdit = QLineEdit(self.frame_2)
        self.wNLineEdit.setObjectName(u"wNLineEdit")

        self.formLayout_3.setWidget(6, QFormLayout.FieldRole, self.wNLineEdit)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.data_phase_1)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_3.setLineWidth(2)
        self.verticalLayout_10 = QVBoxLayout(self.frame_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.list_images = QListWidget(self.frame_3)
        self.list_images.setObjectName(u"list_images")
        self.list_images.setSelectionMode(QAbstractItemView.SingleSelection)
        self.list_images.setItemAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.list_images)


        self.verticalLayout_7.addWidget(self.frame_3)

        self.frame_9 = QFrame(self.data_phase_1)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setSpacing(2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, 2, 2, 2)
        self.btnSeparate = QPushButton(self.frame_9)
        self.btnSeparate.setObjectName(u"btnSeparate")
        icon3 = QIcon()
        iconThemeName = u"emblem-symbolic-link"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.btnSeparate.setIcon(icon3)

        self.verticalLayout_14.addWidget(self.btnSeparate)


        self.verticalLayout_7.addWidget(self.frame_9)


        self.horizontalLayout_4.addWidget(self.data_phase_1)

        self.horizontalLayout_4.setStretch(0, 3)
        self.horizontalLayout_4.setStretch(1, 1)
        self.Process_Phase.addTab(self.get_images, "")
        self.Method_Appliying = QWidget()
        self.Method_Appliying.setObjectName(u"Method_Appliying")
        self.Method_Appliying.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_5 = QHBoxLayout(self.Method_Appliying)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_4 = QFrame(self.Method_Appliying)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_4.setLineWidth(2)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setSpacing(3)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(2, 2, 2, 2)
        self.plotSignalReference = PlotWidget(self.frame_4)
        self.plotSignalReference.setObjectName(u"plotSignalReference")
        sizePolicy8 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(10)
        sizePolicy8.setHeightForWidth(self.plotSignalReference.sizePolicy().hasHeightForWidth())
        self.plotSignalReference.setSizePolicy(sizePolicy8)
        self.plotSignalReference.setMinimumSize(QSize(0, 200))
        self.plotSignalReference.setMaximumSize(QSize(16777215, 200))
        self.plotSignalReference.setLayoutDirection(Qt.LeftToRight)
        self.plotSignalReference.setFrameShape(QFrame.Box)
        self.plotSignalReference.setFrameShadow(QFrame.Raised)
        self.plotSignalReference.setLineWidth(2)
        self.plotSignalReference.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.plotSignalReference.setAlignment(Qt.AlignCenter)
        self.plotSignalReference.setRenderHints(QPainter.Antialiasing|QPainter.TextAntialiasing)
        self.plotSignalReference.setTransformationAnchor(QGraphicsView.NoAnchor)
        self.plotSignalReference.setResizeAnchor(QGraphicsView.AnchorViewCenter)
        self.plotSignalReference.setViewportUpdateMode(QGraphicsView.FullViewportUpdate)

        self.verticalLayout_13.addWidget(self.plotSignalReference)

        self.ImgProcessed = QLabel(self.frame_4)
        self.ImgProcessed.setObjectName(u"ImgProcessed")
        self.ImgProcessed.setFrameShape(QFrame.Box)
        self.ImgProcessed.setFrameShadow(QFrame.Raised)
        self.ImgProcessed.setLineWidth(2)

        self.verticalLayout_13.addWidget(self.ImgProcessed)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.Method_Appliying)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.frame_5.setLineWidth(2)
        self.verticalLayout_11 = QVBoxLayout(self.frame_5)
        self.verticalLayout_11.setSpacing(3)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy6.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy6)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.btnMethod = QPushButton(self.frame_8)
        self.btnMethod.setObjectName(u"btnMethod")

        self.verticalLayout_12.addWidget(self.btnMethod)


        self.verticalLayout_11.addWidget(self.frame_8)

        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 2)
        self.verticalLayout_11.setStretch(2, 1)

        self.horizontalLayout_5.addWidget(self.frame_5)

        self.horizontalLayout_5.setStretch(0, 5)
        self.horizontalLayout_5.setStretch(1, 3)
        self.Process_Phase.addTab(self.Method_Appliying, "")

        self.verticalLayout_9.addWidget(self.Process_Phase)

        self.Process.addTab(self.tabProcessing, "")
        self.tabResult = QWidget()
        self.tabResult.setObjectName(u"tabResult")
        self.Process.addTab(self.tabResult, "")

        self.horizontalLayout_2.addWidget(self.Process)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)

        self.verticalLayout.addWidget(self.Cuerpo)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 975, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuProcess = QMenu(self.menubar)
        self.menuProcess.setObjectName(u"menuProcess")
        self.menuManual = QMenu(self.menuProcess)
        self.menuManual.setObjectName(u"menuManual")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        icon4 = QIcon()
        iconThemeName = u"system-help"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.menuHelp.setIcon(icon4)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuProcess.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuProcess.addAction(self.actionExecute)
        self.menuProcess.addAction(self.menuManual.menuAction())
        self.menuManual.addAction(self.actionImage_Generation)
        self.menuManual.addAction(self.actionLockIn)

        self.retranslateUi(MainWindow)

        self.Process.setCurrentIndex(1)
        self.Process_Phase.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
#if QT_CONFIG(shortcut)
        self.actionExit.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actionExecute.setText(QCoreApplication.translate("MainWindow", u"Automatic", None))
#if QT_CONFIG(shortcut)
        self.actionExecute.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+I", None))
#endif // QT_CONFIG(shortcut)
        self.actionImage_Generation.setText(QCoreApplication.translate("MainWindow", u"Image Generation", None))
        self.actionLockIn.setText(QCoreApplication.translate("MainWindow", u"LockIn", None))
        self.LogoCicata.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">D</span><span style=\" font-size:16pt;\">igital </span><span style=\" font-size:16pt; font-weight:700;\">I</span><span style=\" font-size:16pt;\">maging </span><span style=\" font-size:16pt; font-weight:700;\">T</span><span style=\" font-size:16pt;\">hermography </span><span style=\" font-size:16pt; font-weight:700;\">P</span><span style=\" font-size:16pt;\">rocessing</span></p><p align=\"center\"><span style=\" font-size:16pt;\">Developed  by PhD Eduardo Vargas Bernardino</span></p><p align=\"center\"><span style=\" font-size:16pt;\">CICATA Legaria, IPN, CITNOVA</span></p></body></html>", None))
        self.label_2.setText("")
        self.lblParameters.setText(QCoreApplication.translate("MainWindow", u"Parameters", None))
        self.initFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Init Frame", None))
        self.finalFrameLabel.setText(QCoreApplication.translate("MainWindow", u"Final Frame", None))
        self.modulationLabel.setText(QCoreApplication.translate("MainWindow", u"Modulation", None))
        self.modulation.setSuffix(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.lblInfo.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.framesLabel.setText(QCoreApplication.translate("MainWindow", u"Frames", None))
        self.frameRateLabel.setText(QCoreApplication.translate("MainWindow", u"Frame Rate", None))
        self.frameRate.setSuffix(QCoreApplication.translate("MainWindow", u" fps", None))
        self.frameRate.setPrefix("")
        self.heightLabel.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.framesHeight.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.widthLabel.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.frameWidth.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.frameWidth.setPrefix("")
        self.durationLabel.setText(QCoreApplication.translate("MainWindow", u"Duration:", None))
        self.lblInfo_2.setText(QCoreApplication.translate("MainWindow", u"Method", None))
        self.btnGeometry.setText(QCoreApplication.translate("MainWindow", u"Geometry", None))
        self.btnFourPoints.setText(QCoreApplication.translate("MainWindow", u"Four Points", None))
        self.btnFourier.setText(QCoreApplication.translate("MainWindow", u"Fourier", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Measurement related with", None))
        self.btnRew.setText(QCoreApplication.translate("MainWindow", u"REWIND", None))
        self.btnStart.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.btnStop.setText(QCoreApplication.translate("MainWindow", u"STOP", None))
        self.btnFor.setText(QCoreApplication.translate("MainWindow", u"FORWARD", None))
        self.Process.setTabText(self.Process.indexOf(self.tabVideo), QCoreApplication.translate("MainWindow", u"Video", None))
#if QT_CONFIG(tooltip)
        self.img_p_1_1.setToolTip(QCoreApplication.translate("MainWindow", u"In this frame you can see the gray's scale original image provided by the video", None))
#endif // QT_CONFIG(tooltip)
        self.img_p_1_1.setText("")
#if QT_CONFIG(tooltip)
        self.img_p_1_2.setToolTip(QCoreApplication.translate("MainWindow", u"In this frame you can see the gray's scale original image provided by the video", None))
#endif // QT_CONFIG(tooltip)
        self.img_p_1_2.setText("")
#if QT_CONFIG(tooltip)
        self.img_p_1_3.setToolTip(QCoreApplication.translate("MainWindow", u"In this frame you can see the gray's scale original image provided by the video", None))
#endif // QT_CONFIG(tooltip)
        self.img_p_1_3.setText("")
        self.heightLabel_2.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.heightPhase.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.heightPhase.setPrefix("")
        self.widthLabel_2.setText(QCoreApplication.translate("MainWindow", u"Width", None))
        self.widthPhase.setSuffix(QCoreApplication.translate("MainWindow", u"px", None))
        self.widthPhase.setPrefix("")
        self.framesToProcessLabel.setText(QCoreApplication.translate("MainWindow", u"Frames", None))
        self.framesPerPeriodLabel.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.periodsLabel.setText(QCoreApplication.translate("MainWindow", u"Periods", None))
        self.digital_frequencyLabel.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.wNLabel.setText(QCoreApplication.translate("MainWindow", u"WN", None))
        self.btnSeparate.setText(QCoreApplication.translate("MainWindow", u"Separate", None))
        self.Process_Phase.setTabText(self.Process_Phase.indexOf(self.get_images), QCoreApplication.translate("MainWindow", u"Separate", None))
#if QT_CONFIG(tooltip)
        self.plotSignalReference.setToolTip(QCoreApplication.translate("MainWindow", u"Locking Frequency", None))
#endif // QT_CONFIG(tooltip)
        self.ImgProcessed.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnMethod.setText(QCoreApplication.translate("MainWindow", u"Execute Method", None))
        self.Process_Phase.setTabText(self.Process_Phase.indexOf(self.Method_Appliying), QCoreApplication.translate("MainWindow", u"Applying", None))
        self.Process.setTabText(self.Process.indexOf(self.tabProcessing), QCoreApplication.translate("MainWindow", u"Processing", None))
        self.Process.setTabText(self.Process.indexOf(self.tabResult), QCoreApplication.translate("MainWindow", u"Results", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuProcess.setTitle(QCoreApplication.translate("MainWindow", u"Process", None))
        self.menuManual.setTitle(QCoreApplication.translate("MainWindow", u"Manual", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

