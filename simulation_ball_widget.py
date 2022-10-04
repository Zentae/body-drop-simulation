from graphic_widget import GraphicWidget
from qtpy import QtCore
from qtpy.QtGui import(QPixmap)
from qtpy.QtWidgets import (QLabel)

import time
from lib.stoppable_thread import StoppableThread

class SimulationBall(QLabel):
    """
    Widget representing the bouncing ball animation
    Takes in parameter the simulation's data evolution
    """

    def __init__(self, window) -> None:
        super().__init__(None)
        # inject our window
        self.__window = window
        self._current = None
        # set screen's heigth
        self.__screen_height = window.height()
        # prepare our image
        self.__pixmap = QPixmap("falling-corpses/img/tennis-ball.png")
        self.__pixmap.scaled(10, 10, QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        # prepare our image holder
        self.setScaledContents(True)
        self.setPixmap(self.__pixmap)
        self.setGeometry(470, 0, 120, 100)
    
    def start_animation(self, parameters:list):
        """
        Starts the ball animation.
        Takes in parameter
            - Gravity force
            - Initial speed
            - Restitution coeficient
        """
        self._current = StoppableThread(target=self.__c, args=(parameters,))
        self._current.start()

    def stop_animation(self):
        """
        Stops the ball animation.
        """
        self._current.stop()
        self._current.join()
        self.setGeometry(470, 0, 120, 100)
        # draw our graphic
        self.__draw_graphic(self._current.get_return_value())
    
    def __draw_graphic(self, data:list):
        """
        Draws the graphic with our data
        Takes in parameter a list of list
        """
        # put the data into our graphic
        graphic = GraphicWidget(data[0], data[1])
        graphic.setGeometry(self.__window.width() - 425, 0, 425, self.__window.height())
        self.__window.layout().addWidget(graphic)

    def __c(self, parameters:list):
        # create our time array
        time_array = []
        # create our height array
        height_array = []
        # initial velocity
        v = parameters[0]
        # earth gravity
        g = parameters[1]
        # initial delta time 
        delta_time = 0.0
        # restitution coeficient
        restitution = parameters[2]
        # immutable parameter
        innitial_y = self.__screen_height - 100
        # initial position
        y = self.y()
        while True:
            if v <= -1 and y <= -(self.__screen_height - 100) or self._current.stopped():
                # clean the data
                for i in range(len(height_array)):
                    if height_array[i] < 0:
                        height_array[i] = 0
                # return the data
                self._current.set_return_value([time_array, height_array])
                break
            # fill our time array
            time_array.append(delta_time)
            # fill our height array
            height_array.append((innitial_y + y) * 0.0265)
            time.sleep(0.01)
            v = -v * restitution if y <= -(self.__screen_height - 100) else v + g * delta_time
            y = y - v * delta_time
            delta_time += 0.01
            self.setGeometry(470, abs(y), 120, 100)