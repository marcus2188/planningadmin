from PyQt6.QtWidgets import QCheckBox
from PyQt6.QtCore import QRect, Qt, QSize

class customcheckbox(QCheckBox):
    def __init__(
        self,
        dimensions,
        checkbox_text,
        checked,
        fixed_size = None,
    ):
        super(customcheckbox, self).__init__()
        self.setGeometry(QRect(*dimensions))  # x, y, width, height
        if fixed_size:
            self.setFixedSize(QSize(*fixed_size))
        self.setText(checkbox_text)
        self.setChecked(checked)