import sys

from simulation_window import SimulationWindow
from qtpy.QtWidgets import (QApplication)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = SimulationWindow()
    w.show()
    app.exec_()