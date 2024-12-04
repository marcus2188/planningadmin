from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor
class colorbox(QWidget):
    def __init__(self, color):
        super(colorbox, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)