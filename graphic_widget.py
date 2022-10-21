from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class GraphicWidget(FigureCanvasQTAgg):
    """
    Widget for the graphical representation part
    Takes in parameter the simulation's data evolution
    """
    def __init__(self, x_axis:list, y_axis:list) -> None:
        fig = Figure(figsize=(5, 4), dpi=80)
        self.axes = fig.add_subplot(111)
        self.axes.set_title("Evolution de la hauteur de la balle \n au cours du temps")
        self.axes.set_xlabel("temps (s)")
        self.axes.set_ylabel("hauteur (m)")
        self.axes.plot(x_axis, y_axis)
        super(GraphicWidget, self).__init__(fig)
