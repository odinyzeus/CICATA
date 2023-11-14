from PySide6.QtGui import QPixmap, QImage
import cmath , cv2, sys, math
from cv2.typing import MatLike
from pathlib import Path

class Fourier:
    __method            = 0                  # Indica el methodo de procesamiento 
    __frame_rate        = 0                  # Representa la frecuencia de Muestreo                                                     fs
    __modulation        = 0                  # Representa la frecuencia de Modulacion del experimento                                   fe
    __frame             = 1                  # Frame that is processing actually


    __File_init         = 0                  # Number of initial frame 
    __Final_frame       = 0                  # Final Frame Number
    __current_frame     = None               # Frame (image) is in process
    __listener          = []                 # Se inicializa el controlador de receptores de eventos
    __secuence          = []                 # Contains the secuence of the all images processed 

    __progress_value    = lambda _ , C , F: round((C/F)*100)                            # Calculate the value's progress bar when the frames is precessing
    
    openImage           = lambda _,x: cv2.imread(str(x))                                # Get's the image from the indicated file in path "x" 
    
    def register(self, listener):               # Mètodo que registra a los receptores de eventos de esta clase
        self.__listener.append(listener)
    
    def unregister(self, listener):             # Mètodo que elimina el registro de los receptores de eventos
        self.__listener.remove(listener)
    
    # Funcion que controla el evento de actualizacion de la barra de progreso
    def progressValue(self):
        for observador in self.__listener:
            observador.Progress_changed(self.__progress_value(self.__Cuenta,self.__frames))

    # Raises an event when the image in the current process changes
    def showImage(self, v:QImage):
        for observador in self.__listener:
            observador.Image_changed(v)
    

    # this Function execute the fourier's method 
    def Process(self):








        for i in range(self.Frames):                  # Execute the process for all frames 
            try:
                __filesecond = str(Path(self.__path_file) / Path(f'frame{self.InitialFrame + i}.png').as_posix())
                __img = self.openImage(__filesecond)
                __H, __W , _ = __img.shape                                  # gets the image's dimensions
                # every frame extracted from the original video is loaded    
                

                self.__Cuenta = i + 1
                self.progressValue()
                print (self.W)
                iC = QImage(__img , __W , __H, QImage.Format_Grayscale8)    # convert the image processed to grayscale image
                self.showImage(iC)                                          # Raise the image changed event

            except:
                print(sys.exc_info())


  # Gets the progress's porcentage value of data processing 
    @property
    def Progress_Count(self, value) ->int:
        return self.__Cuenta

    # Gets the number of selected method in the choice box to process the data
    @property
    def Method(self)->int:
        return self.__method

    # Gets the number of frame to be process this value represents the "n" variable for fourier's method
    @property
    def Frames(self)-> int:
        return int(self.FinalFrame - self.InitialFrame)
     
    # Gets the number of periods of the modulation signal that will be processed
    @property
    def Periods(self)-> int:
        return 

    # Gets the frame rate of video to be processed 
    @property
    def FrameRate(self)->int:
        return self.__frame_rate
    
   # Gets the modulation frequency that will be used in the fourier's method
    @property
    def Modulation(self)->  int:
        return self.__modulation
    
   # Gets the number of the initial frame of the set of video's frames to be process
    @property
    def InitialFrame(self)->int:
        return self.__File_init
    
    # Gets the number of frames that integrate the experiment   
    @property
    def FinalFrame(self) ->int:
        return self.__Final_frame

    # Gets the value of delta progress, how many frames represent a 1% of progress
    @property
    def deltaProgress(self)->int:
        return int(self.Frames / 100)

    # Gets the digital frequency of the experiment
    @property
    def K(self)-> int:
        return round(self.FramesByPeriod * (self.Modulation / self.FrameRate) + 1) 
 
    @property
    def WN(self)-> complex:
        return cmath.exp(-1j*2*cmath.pi/self.FramesByPeriod)
   
    @property
    def Frame(self) -> MatLike:
        return self.__current_frame

    @property
    def Frame_all(self) -> list:
        return self.__secuence

    # Sets the progress's porcentage value of data processing 
    @Progress_Count.setter
    def Progress_Count(self, value):
        self.__Cuenta = value
        self.progressValue()

    # Sets the number of selected method in the choice box to process the data, the data will be process only if fourier method is selected 
    # Raise an Method selected is changed event 
    @Method.setter
    def Method(self, value):
        self.__method = value

    # Sets the number of the initial frame of the set of video's frames will be process
    @InitialFrame.setter
    def InitialFrame(self,value):
        self.__File_init = value

    @FinalFrame.setter
    def FinalFrame(self,value):
        self.__Final_frame = value

    # Sets the modulation frequency that will be used in the fourier's method and update the digital frequency automatically
    @Modulation.setter
    def Modulation(self, value):
        self.__modulation = value

    # Sets the frame rate of video to be processed and raise and update the digital frequency automatically
    @FrameRate.setter
    def FrameRate(self, value):
        self.__frame_rate = value

    @Frame.setter
    def Frame(self , value:MatLike):
        t = pow(self.WN,(self.__frame - 1) * (self.K - 1))
        self.__current_frame = value
        print(t)        
        self.__frame =+ 1
        

    def __init__(self, Frames:int = 0 ):
        self.__frames = Frames
        
