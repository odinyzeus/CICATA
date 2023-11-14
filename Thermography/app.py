import sys
import Function.Basics as Basics

from PySide6 import QtWidgets as Wigdets
from PySide6 import QtGui as Gui
from PySide6 import QtMultimedia as Media
from pathlib import Path
from UI.Ui_principal import Ui_MainWindow as Win
from cv2.typing import MatLike


# from Function.Basics import Thermogram as tg , config as cfg
# import Function.Basics as bsf
# from Function.Methods import Fourier as fm

 

# Only needed for access to command line arguments

# Define the main window class
class MainWindow(Wigdets.QMainWindow):
    ui                = Win()

    # Estas variables almacenan la carpeta de trabajo para procesamiento de video y el video a procesar
    __FilePath          = str             # Represents the complete path of the video to process
    __TempPath          = str             # Represents the path of the temporal work area
    mediaPlayer         = Media.QMediaPlayer()
    video               = MatLike # Esta Variable almacena el video para procesamiento por OpenCV
    dataExperiment      = {'FrameRate':int,'Modulation':float,'ModulationPeriod':float,'FramePeriod':int, 'FramesByPeriod':int , 'Periods': int , 'InitFrame': int,'Frames':int}
    count               = int         
    progress            = 0



    Processing          = 0
    ExecuteMethod       = False
    Porcent             = 0
    referenceSenSignal  = None
    referenceCosSignal  = None
    method_selected     = None
    # __thermography      = tg()
    # __fourier_method    = fm()
    
    


    """ Lamda Functions Section"""
    __absPath = lambda _ , p :  str(Path(p).parent) # Returns the absolut path of the file passed


    
    # Se crea el modelo de datos para insertar datos en listas
    listModelItem = Gui.QStandardItemModel()
    
    def __init__(self):
        # construimos el menú
        super().__init__()
        self.ui.setupUi(self)


        self.ui.progressBar.setValue(0)
        self.ui.videoSlider.setValue(0)

        self.ui.actionOpen.triggered.connect(lambda: Basics.openFile(self)) # Se configura la accion del menu para abrir archivo de video 
        self.mediaPlayer.setVideoOutput(self.ui.mediaPlayer)  # Se configura el control que servirà de repoductor multimedia 
        self.ui.frameRate.valueChanged.connect(lambda: Basics.setFrameRate(self))     # Se ejecuta cada que la frecuencia de muestreo del video Cambia
        self.ui.modulation.valueChanged.connect(lambda:Basics.setModulation(self))        # Se ejecuta cada que la frecuencia de modulacion cambia
        self.ui.initFrameSpinBox.valueChanged.connect(lambda: Basics.setInitFrame(self))           # InitFrame
        self.ui.finalFrameSpinBox.valueChanged.connect(lambda: Basics.setFinalFrame(self))         # FinalFrame
        self.ui.btnStart.clicked.connect(lambda: Basics.playvideo(self))
        self.ui.btnStop.clicked.connect(lambda: Basics.stopvideo(self))
        self.ui.btnRew.clicked.connect(lambda: Basics.backvideo(self))
        self.ui.btnFor.clicked.connect(lambda: Basics.forwardvideo(self))
        self.ui.videoSlider.valueChanged.connect(lambda: Basics.move_video(self))
        self.mediaPlayer.positionChanged.connect(lambda: Basics.media_position(self))
        self.ui.progressBar.valueChanged.connect(lambda: Basics.setProgress(self))

        # Se registra la aplicacion como receptor de eventos para la clase que procesa el metodo de fourier
        # self.__fourier_method.register(self)
        # self.__thermography.register(self)

        # validator = Gui.QDoubleValidator()
        # validator.setNotation(Gui.QDoubleValidator.ScientificNotation)

        # self.config = cfg(self.__ui)
        # self.__ui.wNLineEdit.setValidator(validator)

        # # Se configura el evento de seleccionar un archivo de imagen de la lista de images extraidos
        # # self.__ui.list_images.currentItemChanged.connect(functools.partial(bf.firstPhase_imgSelected, self))
        
        
        # # Se configura el widget para graficar las señales de referencia
        # bf.initPlotReference(self.ui.plotSignalReference)

        # # Se configura el boton de processar el methodo thermografico elegido
        # self.__ui.btnMethod.clicked.connect(lambda: bf.execute(self))
        
        # # Se ejecuta cada que se selecciona el metodo de proceso geometrico
        # self.__ui.btnGeometry.clicked.connect(lambda: bf.Method_selected(self, 0))
        
        # # Se ejecuta cada que se selecciona el metodo de proceso de cuatro puntos
        # self.__ui.btnFourPoints.clicked.connect(lambda: bf.Method_selected(self, 1))
    
        # # Se ejecuta cada que se selecciona el metodo de proceso de fourier
        # self.__ui.btnFourier.clicked.connect(lambda: bf.Method_selected(self, 2))
    
    # Se ejecuta cada que se actualiza el valor de la barra de progreso
    def Progress_changed(self, event):
        self.ui.progressBar.setValue(event)

    def Image_changed(self, event):
        self.ui.ImgProcessed.setPixmap(Gui.QPixmap.fromImage(event))
        # self.ui.btnProcesar.clicked.connect(self.procesar)
        # self.ui.p2anLineEdit.textChanged.connect(self.setPValue)
        # self.ui.fRModLineEdit.textChanged.connect(self.setPValue)
        
if __name__ ==  '__main__':
    app = Wigdets.QApplication(sys.argv)
    mi_application = MainWindow()
    mi_application.show()
    sys.exit(app.exec_())