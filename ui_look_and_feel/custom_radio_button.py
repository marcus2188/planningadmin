from PyQt6.QtWidgets import QRadioButton
from PyQt6.QtCore import QRect, Qt, QSize

class customradiobutton(QRadioButton):
    def __init__(
        self,
        dimensions,
        radio_text,
        checked,
        fixed_size = None,
    ):
        super(customradiobutton, self).__init__()
        self.radio_text = radio_text
        self.setGeometry(QRect(*dimensions))  # x, y, width, height
        if fixed_size:
            self.setFixedSize(QSize(*fixed_size))
        self.setText(radio_text)
        self.setChecked(checked)