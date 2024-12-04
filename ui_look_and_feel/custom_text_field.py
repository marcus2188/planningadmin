from PyQt6.QtWidgets import QTextBrowser
from PyQt6.QtCore import QRect, Qt, QSize

class customtextfield(QTextBrowser):
    def __init__(
        self,
        dimensions,
        fixed_size = None
    ):
        super(customtextfield, self).__init__()
        self.setGeometry(QRect(*dimensions))  # x, y, width, height
        self.setPlainText("")
        if fixed_size:
            self.setFixedSize(QSize(*fixed_size))