from PySide6 import QtWidgets as Wigdets
import Function.Basics as Basics
import numpy as np, cmath, cv2
from PySide6.QtGui import QPixmap, QImage
from cv2.typing import MatLike
from pathlib import Path



class Fourier:

    __Frame_Rate        = int                  # Representa la frecuencia de Muestreo                                                     fs
    __modulation        = float                # Representa la frecuencia de Modulacion del experimento                                   fe
    __init_frame        = int
    __FramesByPeriod    = int
    __Frames            = int
    __Experiment        = dict
    __Image_size        = bool
    __count             = 1
    __period            = 1
    
    __listener          = []                 # Se inicializa el controlador de receptores de eventos

    openedImage         = MatLike
    
    WN = lambda _, W,  n, K: pow(W,(n - 1) * (K - 1))

    def register(self, listener):               # Mètodo que registra a los receptores de eventos de esta clase
        self.__listener.append(listener)
    
    def unregister(self, listener):             # Mètodo que elimina el registro de los receptores de eventos
        self.__listener.remove(listener)
    
    @property
    def W(self)->complex:
        return cmath.exp(-1j*2*cmath.pi/self.N)
    
    @property
    def N(self)-> int:
        return self.__FramesByPeriod

    @property
    def FrameRate(self)->int:
        return self.__Frame_Rate
    
    @property
    def Frames(self)->int:
        return self.__Frames

    @property
    def Modulation(self)->float:
        return self.__modulation

    @property
    def K(self)-> int:
       return round(self.N * (self.Modulation / self.FrameRate) + 1)  
    
    @property
    def InitFrame(self)-> int:
        return self.__init_frame
    
    @property
    def Experiment(self)->dict:
        return self.__Experiment
    
    @property
    def ImageFull(self)-> bool:
        return self.__Image_size

    @property
    def Thermogram(self):
        return self.__termograma
    
    @Experiment.setter
    def Experiment(self , value:dict):
        self.__Experiment = value
        self.Frames       = self.__Experiment['Frames']
        self.FrameRate    = self.__Experiment['FrameRate']
        self.N            = self.__Experiment['FramesByPeriod']
        self.Modulation   = self.__Experiment['Modulation']
        self.InitFrame    = self.__Experiment['InitFrame']
        self.__Image_size = self.__Experiment['FullImage']
        self.__Experiment['K'] = self.K
        self.__Experiment['W'] = self.W

        for observador in self.__listener:
            observador.Experiment_Changed(self.__Experiment)

    @ImageFull.setter
    def ImageFull(self, value:bool):
        self.__Image_size = value

    @Modulation.setter
    def Modulation(self, value: float):
        self.__modulation = value

    @N.setter
    def N(self, value: int):
        self.__FramesByPeriod = value

    @Frames.setter
    def Frames(self,value):
        self.__Frames = value

    @FrameRate.setter
    def FrameRate(self, value:int):
        self.__Frame_Rate = value

    @InitFrame.setter
    def InitFrame(self, value:int):
        self.__init_frame = value

    def imgProcess(self , img: MatLike) -> MatLike:
        self.__period = int(self.__count / self.N) + 1
        return img * self.WN(self.W,self.__period,self.K)

    def start(self, video:MatLike,sb : Wigdets.QStatusBar, pg: Wigdets.QProgressBar):
        x,y,_ = self.openedImage.shape()

        video.set(cv2.CAP_PROP_POS_FRAMES , self.InitFrame)   # Se establece la posicion del video en el Frame Inicial
        i = 1 
        while True:
            sb.showMessage(f'Processing frame.:{i}')
            pg.setValue((i+1)*100 /self.Frames)
            ret, self.openedImage = video.read()
            if not ret:
                break
            if self.ImageFull:
                img = self.imgProcess(self.openedImage)
            else:
                self.openedImage = Basics.imgDivide(self.openedImage)
                img = self.imgProcess(self.openedImage)
            i += 1

        sb.showMessage(f'Thermographic lock-in complete.....')
        
    def __init__(self, experiment : dict ):
        self.__Frames = experiment['Frames']
        self.__Frame_Rate = experiment['FrameRate']

    def __init__(self):
        pass
       