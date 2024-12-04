from PyQt6.QtWidgets import QStackedWidget
from PyQt6.QtGui import QPalette, QColor
class stackofpages(QStackedWidget):
    def __init__(self):
        super(stackofpages, self).__init__()
        # self.setAutoFillBackground(True)

        # palette = self.palette()
        # palette.setColor(QPalette.ColorRole.Window, QColor(204, 230, 217))
        # self.setPalette(palette)
        # self.setCurrentIndex(2)