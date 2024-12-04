# This standalone utils script inserts/updates the ini file settings
from PyQt6 import QtCore
import os

if __name__ == "__main__":
    # Switch to cwd and read in .ini file
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    settings = QtCore.QSettings("greatsettings.ini", QtCore.QSettings.Format.IniFormat)

    # Pump in your desired values into the fields (usually blank at first, then set by init_gui_settings() elsewhere )
    settings.setValue("perma_working_dir", "")
    settings.setValue("chosen_ascent_color", "Green")
    settings.setValue("default_ecdgen_name", "")
    settings.setValue("vbs_path_history", "")

    # Verify .ini file by printing out all fields inside it
    keys = settings.allKeys()
    print(keys)
