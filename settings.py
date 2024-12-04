import json
from PyQt6.QtCore import QSettings


def init_gui_settings(mw):
    """Reads in a settings.ini file stored in rootdir/tempdir"""
    settings = QSettings("greatsettings.ini", QSettings.Format.IniFormat)

    # Read chosen_ascent_color str from .ini file
    mw.ss_accent_radio_buttons[
        mw.list_of_accent_colors.index(settings.value("chosen_ascent_color"))
    ].setChecked(True)
    for rb in mw.ss_accent_radio_buttons:
        if rb.isChecked():
            # Change bg colour of sidebar and each pageframe
            mw.central_side_bar.set_color(
                rbg_tuple=mw.mapped_rgb_tuples_to_colors[rb.radio_text]["sidebar"]
            )
            mw.generate_rupture_frame.set_color(
                rbg_tuple=mw.mapped_rgb_tuples_to_colors[rb.radio_text]["pageframe"]
            )
            mw.settings_frame.set_color(
                rbg_tuple=mw.mapped_rgb_tuples_to_colors[rb.radio_text]["pageframe"]
            )
            mw.vbsloader_frame.set_color(
                rbg_tuple=mw.mapped_rgb_tuples_to_colors[rb.radio_text]["pageframe"]
            )

    # Read perma wkdir path from .ini file
    mw.ss_perma_working_dir_text_field.setPlainText(settings.value("perma_working_dir"))

    # Read default_ecdgen_name from .ini file
    mw.ss_ecdgen_filename_text_field.setText(settings.value("default_ecdgen_name"))

    # Read list from vbs path history, set history list and init qlistwidget
    mw.vbs_path_history = (
        json.loads(settings.value("vbs_path_history"))
        if not settings.value("vbs_path_history") == ""
        else []
    )
    mw.vbs_list_widget.addItems(mw.vbs_path_history)
