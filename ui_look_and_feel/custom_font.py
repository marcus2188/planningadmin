from PyQt6.QtGui import QFont

class customfont(QFont):
    def __init__(
        self, 
        font_family,
        font_size
    ):
        super(customfont, self).__init__()
        self.setFamily(font_family)
        self.setPointSize(font_size)
        # test