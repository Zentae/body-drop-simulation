import tkinter
import sys

sys.path.insert(0, 'D:\Développement\Python\Projects\widgets')

from simulation_ball_widget import SimulationBall
from parameter_widget import ParameterWidget

from qtpy.QtWidgets import QMainWindow
from qtpy.QtGui import QCloseEvent

class SimulationWindow(QMainWindow):
    """
    Represents simulation's application main window
    """
    def __init__(self):
        super().__init__(None)
        # set window's title
        self.setWindowTitle("Body fall simulation")
        # get tkinter
        tk = tkinter.Tk()
        # set window's size
        self.setFixedSize(1280, 720)
        self.__s = SimulationBall(self)
        self.__p = ParameterWidget(self.__s)
        # resize the widgets
        self.__p.setGeometry(0, 0, 200, 200)
        # add the widgets
        self.layout().addWidget(self.__p)
        self.layout().addWidget(self.__s)

    def closeEvent(self, a0: QCloseEvent) -> None:
        # check if the thread has been launched
        if(self.__s._current != None):
            # shutdown the simulation thread
            self.__s._current.stop()
        return super().closeEvent(a0)