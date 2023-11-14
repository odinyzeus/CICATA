from UI.Ui_principal import Ui_MainWindow as Win
import pyqtgraph as pg
import functools, math, cv2
import shutil, os ,  time, numpy as np

from PySide6 import QtWidgets as Wigdets
from PySide6 import QtGui as Gui
from PySide6 import QtMultimedia as Media
from PySide6 import QtCore as Core
from pathlib import Path
from cv2.typing import MatLike

# from Function import Methods as mt

# win.digital_frequencySpinBox.setValue(self.fourier_method.K)
# win.wNLineEdit.setText("{:.3f}".format(self.fourier_method.WN.real) + "{:+.3f}".format(self.fourier_method.WN.imag) + "j")

getFramesByPorcentage = lambda x: round(x / 100)
getRangeFrames2Process = lambda x,y: x-y
openImage = lambda x: cv2.imread(str(x))
getPeriods = lambda frames, frame_rate, modulation: frames / (modulation * frame_rate)
getTime = lambda f, fr : divmod(f / fr, 60)


__absFile = lambda p :  str(Path(p).name)   # Returns the file name of the file passed

def setProgress(self):
    if self.ui.progressBar.value() == 100: self.ui.progressBar.setValue(0)

def media_position(self):
    self.ui.videoSlider.setValue(self.mediaPlayer.position())

def move_video(self):
    self.mediaPlayer.setPosition(self.ui.videoSlider.value())

def forwardvideo(self):
    self.mediaPlayer.setPosition(self.mediaPlayer.duration())

def backvideo(self):
    self.mediaPlayer.setPosition(0)

def stopvideo(self):
    if self.mediaPlayer.playbackState() == Media.QMediaPlayer.PlayingState or self.mediaPlayer.playbackState()  == Media.QMediaPlayer.PausedState:
        self.mediaPlayer.stop()

def playvideo(self):
    if self.mediaPlayer.playbackState() == Media.QMediaPlayer.PlayingState:
        self.mediaPlayer.pause()
    else:
        self.mediaPlayer.play()
    self.ui.statusbar.showMessage('Playing Video......')

def setFinalFrame(self):
    calculateFrames(self, self.dataExperiment, self.ui.finalFrameSpinBox , self.ui.initFrameSpinBox, self.ui.framesSpinBox)

def setInitFrame(self):
    calculateFrames(self, self.dataExperiment, self.ui.finalFrameSpinBox , self.ui.initFrameSpinBox, self.ui.framesSpinBox)

def setFrameRate(self):
    self.dataExperiment['FrameRate'] = self.ui.frameRate.value() # Obtenemos el framerate del video

def setModulation(self): 
    self.dataExperiment['Modulation']       = self.ui.modulation.value()
    self.dataExperiment['ModulationPeriod'] = round(1 / self.dataExperiment['Modulation'],3)
    self.dataExperiment['FramePeriod']      = round(1 / self.dataExperiment['FrameRate'],3)    
    self.dataExperiment['FramesByPeriod']   = math.floor(self.dataExperiment['ModulationPeriod'] / self.dataExperiment['FramePeriod'])
    self.dataExperiment['Periods']          = math.floor(self.dataExperiment['Frames'] / self.dataExperiment['FramesByPeriod'])
    
def calculateFrames(self , data : dict, Final: Wigdets.QSpinBox, Init: Wigdets.QSpinBox, Frames: Wigdets.QSpinBox):
    data['InitFrame'] = Init.value()
    data['Frames']    = Final.value() - Init.value()
    Frames.setValue(data['Frames'])
    openVideo(self.video, data, self.ui.statusbar)

def enablePlayerButtons(window:Win, value: bool)-> None:
    window.btnRew.setEnabled(value)
    window.btnStart.setEnabled(value)
    window.btnStop.setEnabled(value)
    window.btnFor.setEnabled(value)
    window.btnSeparate.setEnabled(value)

"""
    This function check at the temp folder exist and its VAcio
    if the folder doesn`t exist its created.
"""
def checkTempFolder(self):
    self.__TempPath = Path(self.__absPath(self.__FilePath)) / 'temp'
    shutil.rmtree(self.__TempPath, ignore_errors=True)
    os.makedirs(self.__TempPath)

""" 
    This function open the video to be process
"""
def openVideo(video : cv2.VideoCapture, data : dict, sb : Wigdets.QStatusBar) -> MatLike: 
    video.set(cv2.CAP_PROP_POS_FRAMES , data['InitFrame'] - 1)   # Se establece la posicion del video en el Frame Inicial
    sb.showMessage(f'Frame Init has been established to frame No.:{int(video.get(cv2.CAP_PROP_POS_FRAMES))}')  
                

"""
    This function presents a dialog windows to open the video file to be process
"""
def openFile(self):
    self.__FilePath , _ = Wigdets.QFileDialog.getOpenFileName(self,"Abrir archivo", str("Videos (*.avi *.mp4)"))
    self.ui.statusbar.showMessage('Openning the Video......')
    self.mediaPlayer.setSource(Core.QUrl(self.__FilePath))                          # set the file like source of video
    self.ui.videoSlider.setMaximum(self.mediaPlayer.duration())     # Set the Video player slider to maximum value of video's duration
    enablePlayerButtons(self.ui, True)                                 # Enable the video player controls
    checkTempFolder(self)

    self.video = cv2.VideoCapture(self.__FilePath)
    t = int(self.video.get(cv2.CAP_PROP_FRAME_COUNT))
    self.ui.initFrameSpinBox.setMaximum(t)
    self.ui.finalFrameSpinBox.setMaximum(t)
    self.ui.finalFrameSpinBox.setValue(t)
    self.ui.framesSpinBox.setMaximum(t)
    t = int(self.video.get(cv2.CAP_PROP_FPS))
    self.ui.frameRate.setMaximum(t)
    self.ui.frameRate.setValue(t)
    self.ui.framesHeight.setValue(int(self.video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
    self.ui.frameWidth.setValue(int(self.video.get(cv2.CAP_PROP_FRAME_WIDTH)))

    # Se calcula el tiempo de duracion del video
    __MinutesGet, __SecondsGet = getTime(self.ui.finalFrameSpinBox.value(), self.ui.frameRate.value())
    self.ui.duration.setText(Core.QCoreApplication.translate("MainWindow", str(f'{round(__MinutesGet)}:{round(__SecondsGet)}'), None))

"""_summary_
    This Function obtains the RGB and grayscale Channels of a thermal image, then converts the rgb portion to grayscale
    and finally merges both grayscale images into weighted image one.
"""
def RGBSepareProcess(img):
    # convertimos la imagen seleccionada a escala de grises
    __img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    # Obtenemos las dimensiones iniciales de la imagen
    __H, __W , _ = img.shape
    __H = int(__H/ 2)

    # segmentamos la Imagen en gris en las dos imagenes que la componen
    __iA = __img[:__H,:]
    __iB = __img[__H:,:]

    __A = img[:__H,:]
    __B = img[__H:,:]

    __I = cv2.addWeighted(__iA, 0.5, __iB, 0.5, 0) # Fusionar las imágenes con un peso de 0.5 para cada una

    # Apllicamos una normalizaciòn a la imagen
    # __I = cv2.equalizeHist(__I)

    # """
    #      Ejecutamos el proceso de ecualizacion de la imagen, esto elimimina la sobre iluminacion
    #      para esto emplearemos un kernel de 5,5
    # """

    clahe= cv2.createCLAHE(clipLimit=0.5, tileGridSize=(3,3))  # se crea la configuraciòn del filtro
    __I = clahe.apply(__I)

    """
    # Este segmento de codigo nos permite umbralizar la imagen
    # esta parte nos permitiria definir con claridad los  contornos que genera el gradiente de temperatura
    __krn = 155
    __const= 0
    __I = cv2.adaptiveThreshold(__I,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,__krn,__const)
    """

    # Se procesan las imagenes segmentadas para mostrarlas en la UI
    iA = QImage(__A , __W , __H, QImage.Format_RGB888)
    iB = QImage(__B , __W , __H, QImage.Format_RGB888)
    iC = QImage(__I , __W , __H, QImage.Format_Grayscale8)

    return int(__H) , int(__W) , np.uint8(__I)  ,  iA, iB , iC

def firstPhase_imgSelected(self, nuevo, anterior):
    # abrimos la imagen contenida en el archivo seleccionado
    __file = win.list_images.currentItem().text() + '.png'
    __file = self.firstFolder.joinpath(__file)
    __img = openImage(__file)


    # se procesa la imagen cargada
    __H, __W , _, __A , __B , __C = RGBSepareProcess(__img)

    # # Presentamos la imagen cargada en la UI
    win.img_p_1_1.setPixmap(QPixmap.fromImage(__A))
    win.img_p_1_2.setPixmap(QPixmap.fromImage(__B))
    win.img_p_1_3.setPixmap(QPixmap.fromImage(__C))

def referenceX(self):
    # Generamos el vector de puntos de la señal de referencia
    return np.linspace(0, self.fourier_method.Frames, self.fourier_method.Frames)

def referenceSen(self):
    return np.sin(2 * np.pi * self.fourier_method.Modulation * referenceX())

def referenceCos(self):
    return np.cos(2 * np.pi * self.fourier_method.Modulation * referenceX())
















def list_Fill(self, item):
    __item = absFile(item)
    win.list_images.addItem(QListWidgetItem(__item))
       

        





"""
    # Se grafican las señales de referencia para que el usuario observe de forma visual la referencia que serà usada
    # Se borran las señales anteriores
    win.plotSignalReference.clear()

    win.plotSignalReference.setXRange(0,muestras)                                 # Se  determina el rango del eje X
    win.plotSignalReference.plot(self.referenceSenSignal, name='Seno', pen = pg.mkPen('b',width = 3))    # Se grafica la primera señal de referencia con linea de color azul
    win.plotSignalReference.plot(self.referenceCosSignal, name='Coseno', pen = pg.mkPen('g',width = 3))  # Se grafica la seguna señal de referencia con linea de color verde
    win.periods.setValue(getPeriods(muestras, frame_rate,frequency))
"""

def initprocess(self):
    win.statusbar.showMessage('Extracting frames.............')
    
    # Se define el contador de frames procesados del video, asi como el procentaje de avance en la barra de progreso
    __ct = 1
    __x  = 0
    
    # Se definen las variables internas para el tamaño de imagen y adicionales
    __H = int(0)
    __W = int(0)

    # Obtenemos la imagen desde el video bajo analisis
    while True:
        ret , im = self.capture.read()
        if not ret:
            break
        else:
            if win.initFrameSpinBox.value() <= __ct <= win.finalFrameSpinBox.value():
                # Generamos el nombre del archivo para la imagen extraida
                __filefirst = str(Path(self.firstFolder) / Path(f'frame{__ct}.png').as_posix())
                __filesecond = str(Path(self.secondFolder) / Path(f'frame{__ct}.png').as_posix())
            
                # Inserta el nombre de archivo en la lista de imagenes extraidas
                list_Fill(self, Path(__filefirst).stem)
            
                # Se guarda el fotograma extraido en RGB como archivo de imagen independiente formato png
                cv2.imwrite(__filefirst, im)
            
                # Se procesa el fotograma, para convertirlo en escala de grises y fundir la parte a color
                __H, __W , __I, _ , _ , _ = RGBSepareProcess(im)

                # la imagen resultante se guarda en la carpeta temporal de segunda fase
                cv2.imwrite(__filesecond,__I)
                # En este segmento de codigo se determina que la barra de progreso avance 1% cada que se han procesado el numero de frames
                # Correspondientes al 1% del total de frames bajo analisis
                setProgress(self,__x) 
                      
            __x += 1
            __ct += 1

    # Se muestran las dimensiones de la imagen procesada en la Interface de usuario
    win.heightPhase.setValue(__H)
    win.widthPhase.setValue(__W)   
    
    win.statusbar.showMessage('Frames Extracted.............')         

def initPlotReference(self: pg.PlotWidget):
    # Se configuran el color de fondo y parametros bàsicos de las graficas de las señales de referencia
    self.setBackground("w")
    self.addLegend()
    self.setTitle('Reference Signals', size = '20px')
    self.setLabel('left','Amplitude')
    self.setLabel('bottom','Frames',size = '12px')


# This Function execute the selected method's analisys
def execute(self):
    # str( / Path(f'frame{__ct}.png').as_posix())
    __m = ''
    if self.fourier_method.Method == 0:
        pass
    if self.fourier_method.Method == 1:
        pass
    if self.fourier_method.Method == 2:
         __m = 'Fourier'
         self.fourier_method.Process()

         
    win.statusbar.showMessage(f'Thermographics lock in using {__m} Executing.............')
    