# THIS IS THE PLACE STORING ALL DATA, CONSTANTS, AND LOOKUPS for code
class single_source_of_truth:
    """List of files to browse to generate rupture"""

    generate_rupture_files_required = [
        "Opening SOH",
        "ZC32",
        "Prod Vol",
        "DN",
        "Stock Transfer"
    ]

    """ LHS is keywords to find in filename, RHS is the filetype """
    mapped_sap_file_to_filetype = {
        "OPENING SOH": "Opening SOH",
        "ZC32": "ZC32",
        "PROD VOL": "Prod Vol",
        "ZC48": "DN",
        "H978": "Stock Transfer"
    }
    """ Contains all correct column names of each file """
    ecd_file_correct_columns = {
        "SO": [
            "Material Number",
            "Mat.Description",
            "Open Qty.",
            "First Delivery date",
            "Name",
            "Doc. Date",
            "Sales Document",
            "P.O Number",
            "Item No",
            "Reason For Rejection",
        ],
        "SOH": ["Material", "Material Description", "Unrestricted", "Plant"],
        "Conrel": [
            "Traffic light",
            "Ship-To Party",
            "Originating Document",
            "Material",
            "Description",
            "Open quantity",
            "Plant",
            "Distribution Channel",
            "Deliv. Creation Date",
        ],
        "DN": [
            "Delivery",
            "Deliv. date(From/to)",
            "Material",
            "Description",
            "Delivery quantity",
            "Name of sold-to party",
        ],
        "OISL": [
            "Material",
            "Short Text",
            "Order Quantity",
            "Delivery date",
            "Purchasing Document",
        ],
        "ZC32CS": [
            "Sal Ty",
            "Sales Document",
            "Doc. Date",
            "P.O Number",
            "Plant",
            "Name",
            "Name.1",
            "Name of the district",
            "Item No",
            "Material Number",
            "Mat.Description",
            "Open Qty.",
            "Open Qty. MT",
            "Net-price",
            "Net-Value",
            "First Delivery date",
            "Delivery Status",
            "Overall Blkd Status",
            "Reason For Rejection",
        ],
        "Prev ECD": [
            "Primary Key",
            "Purchasing Document",
            "Sal Ty",
            "Sales Document",
            "Doc. Date",
            "P.O Number",
            "Plant",
            "Name",
            "Name.1",
            "Name of the district",
            "Item No",
            "Material Number",
            "Mat.Description",
            "Open Qty.",
            "Open Qty. MT",
            "Net-price",
            "Net-Value",
            "First Delivery date",
            "Delivery Status",
            "Overall Blkd Status",
            "ECD Status",
            "Comments",
        ],
        "material_to_weight_mapping_table.xlsx": [
            "Material",
            "Material Description",
            "Net weight",
            "Volume",
            "Pack Size",
        ],
        "material_to_cat_mapping_table.xlsx": [
            "Code",
            "Description",
            "Product Cat",
            "MOQ",
            "Lead Time in days",
            "Category",
            "Source",
        ],
    }

    """ Generate rupture """
    # page menu buttons list
    generate_rupture_page_menu_button_names = ["Auto Find Files", "Clear All"]

    # SO DN sheet aggregate table header names
    aggregate_table_names = ["SO", "DN", "SO/DN"]

    # zc32 sheet orange columns (handpicked columns to be shaded orange)
    zc32_sheet_orange_columns = [
        "Primary Key",
        "Purchasing Document",
        "ECD Status",
        "Comments",
    ]

    """ App theme colour names """
    app_theme_colour_names = ["Green", "Red", "Blue", "Purple", "Orange"]

    """ Colour mapping applied to sidebar and frames """
    mapped_rgb_tuples_to_colors = {
        "Green": {"sidebar": (143, 189, 166), "pageframe": (225, 225, 225)},
        "Red": {"sidebar": (173, 85, 135), "pageframe": (225, 225, 225)},
        "Blue": {"sidebar": (79, 131, 168), "pageframe": (200, 200, 200)},
        "Purple": {"sidebar": (135, 92, 181), "pageframe": (225, 225, 225)},
        "Orange": {"sidebar": (255, 173, 51), "pageframe": (225, 225, 225)},
    }
    
    """ Sidebar button standarised style """
    sidebar_buttontext_colour = "white" # colour in css colour str
    sodebar_button_transparency = 30   # transparency as percentage% of 100 percent
    
    """ Page frames button standardised style """
    page_buttontext_colour = "white" # colour in css colour str
    page_button_transparency = 48   # transparency as percentage% of 100 percent
