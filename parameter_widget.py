# import the container for the parameters
from simulation_ball_widget import SimulationBall
from qtpy.QtWidgets import (QVBoxLayout, QWidget, QDoubleSpinBox, QLabel, QPushButton)

class ParameterWidget(QWidget):
    """
    Widget for the parameters part.
    Takes in parameter a parameter container for the simulation.
    """
    def __init__(self, ball:SimulationBall) -> None:
        super().__init__()
        # save the ball in cache
        self.__ball = ball
        # set widget's layout
        self.__layout = QVBoxLayout()
        # set initial speed selection
        self.__speed_label = QLabel("Vitesse initiale (m/s)")
        self.__speed_spin_box = QDoubleSpinBox()
        self.__speed_spin_box.setSingleStep(.01)
        # set gravity selection
        self.__gravity_label = QLabel("Gravité (m/s^2)")
        self.__gravity_spin_box = QDoubleSpinBox()
        self.__gravity_spin_box.setSingleStep(.01)
        self.__gravity_spin_box.setMinimum(.01)
        # set default value as earth gravity
        self.__gravity_spin_box.setValue(9.807)
        # set restitution coefficient selection
        self.__coefficient_label = QLabel("Coéfficient de restitution")
        self.__coefficient_spin_box = QDoubleSpinBox()
        # set coefficient minimum & maximum value
        self.__coefficient_spin_box.setValue(0.6)
        self.__coefficient_spin_box.setRange(.1, 1.)
        self.__coefficient_spin_box.setSingleStep(.01)
        # set the start button.
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.__start_animation_wrapper)
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.__stop_animation_wrapper)
        # disable the button a start
        self.stop_button.setEnabled(False)
        # add sub-widgets
        self.__layout.addWidget(self.__speed_label)
        self.__layout.addWidget(self.__speed_spin_box)
        self.__layout.addWidget(self.__gravity_label)
        self.__layout.addWidget(self.__gravity_spin_box)
        self.__layout.addWidget(self.__coefficient_label)
        self.__layout.addWidget(self.__coefficient_spin_box)
        self.__layout.addWidget(self.start_button)
        self.__layout.addWidget(self.stop_button)
        # select widget's layout
        self.setLayout(self.__layout)

    def __start_animation_wrapper(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        list = [self.__speed_spin_box.value(), self.__gravity_spin_box.value(), self.__coefficient_spin_box.value()]
        self.__ball.start_animation(list)
    
    def __stop_animation_wrapper(self):
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.__ball.stop_animation()