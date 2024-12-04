from PyQt6.QtWidgets import QFrame
from PyQt6.QtGui import QPalette, QColor
class customframe(QFrame):
    def __init__(
        self,
        rbg_tuple = None,
        color_text = None
    ):
        super(customframe, self).__init__()
        self.set_color(rbg_tuple, color_text)
    
    def set_color(
        self,
        rbg_tuple = None,
        color_text = None
    ):
        if rbg_tuple or color_text:
            self.setAutoFillBackground(True)
            palette = self.palette()
            if rbg_tuple:
                palette.setColor(QPalette.ColorRole.Window, QColor(*rbg_tuple))
            else:
                palette.setColor(QPalette.ColorRole.Window, QColor(color_text))
            self.setPalette(palette)
        
