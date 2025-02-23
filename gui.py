from PyQt6.QtWidgets import (
    QMainWindow,
    QGridLayout,
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QProgressBar,
    QPushButton,
    QLineEdit,
)
from frames.custom_frame import customframe
from stacked_widgets.page_stack import stackofpages
from buttons.custom_button import custombutton
from labels.custom_label import customlabel
from data import single_source_of_truth
from ui_look_and_feel.custom_text_field import customtextfield
from ui_look_and_feel.custom_checkbox import customcheckbox
from ui_look_and_feel.custom_radio_button import customradiobutton
from widgets.progress_widget import progressBox


class planningadmin_mainwindow(QMainWindow):
    """Design the layout and UI of the entire app here"""

    def __init__(self):
        super(planningadmin_mainwindow, self).__init__()

        # Main window options
        self.resize(1200, 600)
        self.setWindowTitle("PLANNING-ADMIN V1.7")

        # ------------ Central widget building here -----------
        # Steps: Define Layout -> Add in elements -> Set layout

        """ 
        Define central widget and central widget grid
        Add sidebar and stack_of_pages to main grid layout
        Set the grid layout on central widget itself
        """
        self.central_widget = QWidget()
        self.main_grid_layout = QGridLayout()
        self.main_grid_layout.setSpacing(0)
        self.main_grid_layout.setContentsMargins(0, 0, 0, 0)
        self.central_side_bar = customframe()
        self.main_grid_layout.addWidget(self.central_side_bar, 0, 0, 1, 1)
        self.central_stack_of_pages = stackofpages()
        self.main_grid_layout.addWidget(self.central_stack_of_pages, 0, 1, 1, 4)
        self.central_widget.setLayout(self.main_grid_layout)
        self.setCentralWidget(self.central_widget)

        """ 
        Create title label and sidebar buttons
        Define vbox layout in sidebar
        Set the vbox layout on side bar itself
        """
        self.title_label = customlabel(
            displaytext="Planning\nAdmin",
            dimensions=(20, 20, 20, 20),
            desired_font=("Courier New", 40),
            stylised=True,
        )
        self.generate_rupture_button = custombutton(
            buttontext="Rupture Report",
            dimensions=(20, 20, 70, 40),
            desired_font=("Trebuchet MS", 16),
            buttontext_colour = single_source_of_truth.sidebar_buttontext_colour,
            button_transparency = single_source_of_truth.sodebar_button_transparency,
        )
        self.vbsloader_button = custombutton(
            buttontext="Vbs Loader",
            dimensions=(20, 20, 70, 40),
            desired_font=("Trebuchet MS", 16),
            buttontext_colour = single_source_of_truth.sidebar_buttontext_colour,
            button_transparency = single_source_of_truth.sodebar_button_transparency,
        )
        self.settings_button = custombutton(
            buttontext="Settings",
            dimensions=(20, 20, 70, 40),
            desired_font=("Trebuchet MS", 16),
            buttontext_colour = single_source_of_truth.sidebar_buttontext_colour,
            button_transparency = single_source_of_truth.sodebar_button_transparency,
        )
        self.vbox_side_bar = QVBoxLayout()
        self.vbox_side_bar.addStretch()
        self.vbox_side_bar.addWidget(self.title_label)
        self.vbox_side_bar.addStretch()
        self.vbox_side_bar.addWidget(self.generate_rupture_button)
        self.vbox_side_bar.addStretch()
        self.vbox_side_bar.addWidget(self.vbsloader_button)
        self.vbox_side_bar.addStretch()
        self.vbox_side_bar.addWidget(self.settings_button)
        self.vbox_side_bar.addStretch()
        self.central_side_bar.setLayout(self.vbox_side_bar)

        """ 
        Add pageframes to each central stacked page
        generate rupture page - light green
        vbs loader page - xx
        settings page - red
        """
        self.generate_rupture_frame = customframe()
        self.vbsloader_frame = customframe(color_text="red")
        self.settings_frame = customframe()
        self.central_stack_of_pages.addWidget(self.generate_rupture_frame)
        self.central_stack_of_pages.addWidget(self.vbsloader_frame)
        self.central_stack_of_pages.addWidget(self.settings_frame)

        """
        Create all generate rupture page buttons, textfields
        list: so, soh, conrel, dn, oisl, zc32cslayout
        Create Generate rupture button itself
        Create a grid layout inside each stacked pageframe: 7 x 8, w x h
        """
        self.list_of_menus = single_source_of_truth.generate_rupture_page_menu_button_names
        self.gr_menu_buttons = [
            custombutton(
                buttontext=x,
                dimensions=(20, 20, 80, 30),
                desired_font=("Trebuchet MS", 12),
                buttontext_colour = single_source_of_truth.page_buttontext_colour,
                button_transparency = single_source_of_truth.page_button_transparency,
            )
            for x in self.list_of_menus
        ]
        self.list_of_files_to_browse = (
            single_source_of_truth.generate_rupture_files_required
        )
        self.gr_browse_buttons = [
            custombutton(
                buttontext=x,
                dimensions=(20, 20, 80, 40),
                desired_font=("Trebuchet MS", 12),
                buttontext_colour = single_source_of_truth.page_buttontext_colour,
                button_transparency = single_source_of_truth.page_button_transparency,
            )
            for x in [f"Browse for {y}" for y in self.list_of_files_to_browse]
        ]
        self.gr_browse_text_fields = [
            customtextfield(dimensions=(160, 160, 60, 10), fixed_size=(300, 40))
            for _ in self.list_of_files_to_browse
        ]
        self.gr_generate_rupture_button = custombutton(
            buttontext="Generate",
            dimensions=(20, 20, 100, 40),
            desired_font=("Trebuchet MS", 30),
            buttontext_colour = single_source_of_truth.page_buttontext_colour,
            button_transparency = single_source_of_truth.page_button_transparency,
        )

        # Adding elements into the generate ecd page grid
        self.gr_generate_rupture_frame_grid = QGridLayout()
        for ind in range(len(self.list_of_menus)):
            self.gr_generate_rupture_frame_grid.addWidget(
                self.gr_menu_buttons[ind], 0, ind + 2, 1, 1
            )
        for ind in range(len(self.list_of_files_to_browse)):
            if ind <= 3:
                self.gr_generate_rupture_frame_grid.addWidget(
                    self.gr_browse_buttons[ind], ind + 1, 0, 1, 1
                )
                self.gr_generate_rupture_frame_grid.addWidget(
                    self.gr_browse_text_fields[ind], ind + 1, 1, 1, 3
                )
            else:
                self.gr_generate_rupture_frame_grid.addWidget(
                    self.gr_browse_buttons[ind], (ind % 4) + 1, 4, 1, 1
                )
                self.gr_generate_rupture_frame_grid.addWidget(
                    self.gr_browse_text_fields[ind], (ind % 4) + 1, 5, 1, 3
                )

        self.gr_generate_rupture_frame_grid.addWidget(
            self.gr_generate_rupture_button, 5, 0, 1, 8
        )
        self.generate_rupture_frame.setLayout(self.gr_generate_rupture_frame_grid)

        """
        Create all settings page buttons, textfields
        Create grid layout
        Set the grid layout on the settings page frame
        """
        ###### acl -> ss_ascent_color_label
        self.ss_ascent_color_label = customlabel(
            displaytext="Ascent Color:",
            dimensions=(20, 20, 20, 20),
            desired_font=("Trebuchet MS", 15),
        )
        ###### pwdl -> ss_perma_working_dir_label
        self.ss_perma_working_dir_label = customlabel(
            displaytext="Permanent Dir:",
            dimensions=(20, 20, 20, 20),
            desired_font=("Trebuchet MS", 15),
        )
        self.list_of_accent_colors = single_source_of_truth.app_theme_colour_names
        self.mapped_rgb_tuples_to_colors = (
            single_source_of_truth.mapped_rgb_tuples_to_colors
        )
        ###### acrb -> ss_accent_radio_button
        self.ss_accent_radio_buttons = [
            customradiobutton(
                dimensions=(20, 20, 100, 40), 
                radio_text=x, 
                checkbox_colour=single_source_of_truth.mapped_rgb_tuples_to_colors[x]["sidebar"], 
                checked=False
            )
            for x in self.list_of_accent_colors
        ]
        ###### pwdt -> ss_perma_working_dir_text_field
        self.ss_perma_working_dir_text_field = customtextfield(
            dimensions=(160, 160, 100, 10), fixed_size=(350, 35)
        )
        ###### pwdb -> ss_browse_permadir_button
        self.ss_browse_permadir_button = custombutton(
            buttontext="Change",
            dimensions=(20, 20, 100, 40),
            desired_font=("Trebuchet MS", 12),
            buttontext_colour = single_source_of_truth.page_buttontext_colour,
            button_transparency = single_source_of_truth.page_button_transparency,
        )
        ###### pwdc -> ss_clear_permadir_button
        self.ss_clear_permadir_button = custombutton(
            buttontext="Clear",
            dimensions=(20, 20, 100, 40),
            desired_font=("Trebuchet MS", 12),
            buttontext_colour = single_source_of_truth.page_buttontext_colour,
            button_transparency = single_source_of_truth.page_button_transparency,
        )
        ###### egfl -> ss_ecdgen_filename_label
        self.ss_ecdgen_filename_label = customlabel(
            displaytext="Default ecdgen\nname\nexcluding '.xlsx':",
            dimensions=(20, 20, 20, 20),
            desired_font=("Trebuchet MS", 15),
        )

        ###### egft -> ss_ecdgen_filename_text_field
        self.ss_ecdgen_filename_text_field = QLineEdit()
        self.ss_ecdgen_filename_text_field.setText("newgeneratedfile")
        self.ss_ecdgen_filename_text_field.setStyleSheet("""
            QLineEdit {
                background-color: #FAFAFA;        /* Light background */
                color: #212121;                   /* Dark text */
                border: 1px solid #E0E0E0;        /* Light gray border */
                border-radius: 8px;               /* Rounded corners */
                padding: 4px;                     /* Comfortable padding */
                font-family: 'Trebuchet MS', sans-serif; /* Material font */
                font-size: 12px;                  /* Slightly larger font size */
                line-height: 1;                 /* Improved line spacing */
            }

            QLineEdit {
                min-height: 30px;                 /* Minimum height to make the input box bigger */
            }
        """)

        ###### egsl -> ss_ecdgen_save_label
        self.ss_ecdgen_save_label = customlabel(
            displaytext="(Click to Edit,\nhit Enter to Save)",
            dimensions=(20, 20, 20, 20),
            desired_font=("Trebuchet MS", 15),
        )

        # Representation of settings page grid: (4x5), max acronym length = 4
        ###### x -> blank space
        ## ************************************
        ## x,    x,    x,    x,    x
        ## acl,  acrb, acrb, acrb, acrb
        ## pwdl, <  pwdt  >, pwdb, pwdc
        ## egfl, <  egft  >, egsl, x
        ## ************************************
        self.ss_frame_grid = QGridLayout()
        self.ss_frame_grid.addWidget(self.ss_ascent_color_label, 1, 0, 1, 1)
        for ind in range(len(self.list_of_accent_colors)):
            self.ss_frame_grid.addWidget(
                self.ss_accent_radio_buttons[ind], 1, ind + 1, 1, 1
            )
        self.ss_frame_grid.addWidget(self.ss_perma_working_dir_label, 2, 0, 1, 1)
        self.ss_frame_grid.addWidget(self.ss_perma_working_dir_text_field, 2, 1, 1, 2)
        self.ss_frame_grid.addWidget(self.ss_browse_permadir_button, 2, 3, 1, 1)
        self.ss_frame_grid.addWidget(self.ss_clear_permadir_button, 2, 4, 1, 1)
        self.ss_frame_grid.addWidget(self.ss_ecdgen_filename_label, 3, 0, 1, 1)
        self.ss_frame_grid.addWidget(self.ss_ecdgen_filename_text_field, 3, 1, 1, 2)
        self.ss_frame_grid.addWidget(self.ss_ecdgen_save_label, 3, 3, 1, 1)
        self.settings_frame.setLayout(self.ss_frame_grid)

        """
        Init the vbs loader page layout
        """

        self.vb_menu_buttons = [
            custombutton(
                buttontext=x,
                dimensions=(20, 20, 80, 30),
                desired_font=("Trebuchet MS", 12),
                buttontext_colour = single_source_of_truth.page_buttontext_colour,
                button_transparency = single_source_of_truth.page_button_transparency,
            )
            for x in ["Browse", "Clear All"]
        ]
        self.vbs_path_history = []
        self.vbs_list_widget = QListWidget()
        self.vbs_list_widget.addItems(self.vbs_path_history)
        self.vb_runvbs_button = custombutton(
            buttontext="Run VBS",
            dimensions=(20, 20, 100, 40),
            desired_font=("Trebuchet MS", 30),
            buttontext_colour = single_source_of_truth.page_buttontext_colour,
            button_transparency = single_source_of_truth.page_button_transparency,
        )
        # Adding elements into the vbs loader page grid
        self.vb_vbloader_frame_grid = QGridLayout()
        for ind, _ in enumerate(self.vb_menu_buttons):
            self.vb_vbloader_frame_grid.addWidget(
                self.vb_menu_buttons[ind], 0, ind + 1, 1, 1
            )
        self.vb_vbloader_frame_grid.addWidget(self.vbs_list_widget, 1, 0, 1, 4)
        self.vb_vbloader_frame_grid.addWidget(self.vb_runvbs_button, 3, 0, 1, 4)
        self.vbsloader_frame.setLayout(self.vb_vbloader_frame_grid)

        """ Init a shared progress window instance for generating ecd """
        self.progress_window = progressBox(0, "", "In Progress", None)


def init_gui_elements():
    new_planningadmin_window = planningadmin_mainwindow()
    return new_planningadmin_window
