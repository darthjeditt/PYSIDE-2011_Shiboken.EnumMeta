# -*- coding: utf-8 -*-
'''Global PROXi stylesheet'''


STYLESHEET = """

    /*
        [Environ variable]              [Description]
        QTMATERIAL_PRIMARYCOLOR         Primary color
        QTMATERIAL_PRIMARYLIGHTCOLOR    A bright version of the primary color
        QTMATERIAL_SECONDARYCOLOR       Secondary color 
        QTMATERIAL_SECONDARYLIGHTCOLOR  A bright version of the secondary color
        QTMATERIAL_SECONDARYDARKCOLOR   A dark version of the primary color
        QTMATERIAL_PRIMARYTEXTCOLOR     Color for text over primary background
        QTMATERIAL_SECONDARYTEXTCOLOR   Color for text over secondary background
        QTMATERIAL_THEME                Name of theme used
    */


    /*
        Use font-weight 500 for semi-bold and 800 for bold. Default bold weight is 700, which renders poorly for some reason
    */


    *, 
    QPushButton, 
    QTabWidget, 
    QWidget {{
        font-weight: normal;
        text-transform: none;
    }}

    QTabBar {{
        font-size: 14px;
        font-weight: 500;
        text-transform: uppercase;
    }}

    QTabBar::tab:top:selected {{
        color: #FF9800;
        border-bottom: 2px solid #FF9800;
    }}

    QTabBar::tab:top:!selected:hover {{
        color: #FF9800;
        border-bottom: 2px solid #FF9800;
    }}

    QTabBar::tab:top:disabled {{
        color: #858585;
        text-decoration: line-through;
    }}

    QPushButton {{
        color: {QTMATERIAL_SECONDARYCOLOR};
        font-size: 15px;
        background-color: {QTMATERIAL_PRIMARYCOLOR};
        font-weight: 500;
    }}

    QPushButton:checked,
    QPushButton:pressed {{
        color: {QTMATERIAL_SECONDARYCOLOR};
        background-color: {QTMATERIAL_PRIMARYLIGHTCOLOR};
        border-color: {QTMATERIAL_PRIMARYLIGHTCOLOR};
    }}

    QPushButton QLabel {{
        color: {QTMATERIAL_SECONDARYCOLOR}
    }}

    QComboBox,
    QLineEdit {{
        /*color: #b9b9b9;*/
        color: {QTMATERIAL_SECONDARYTEXTCOLOR};
    }}

    QComboBox,
    QLineEdit,
    QComboBox:disabled,
    QLineEdit:disabled {{
        border: none;
        border-radius: 4px;
    }}

    QComboBox {{
        height: 32px;
    }}

    QGroupBox {{
        padding: 10px;
    }}

    QLineEdit,
    QLineEdit:disabled,
    QPlainTextEdit,
    QComboBox {{
        padding-left: 8px;
        padding-right: 8px;
    }}
    QComboBox {{
        padding-left: 10px;
    }}
    QPlainTextEdit {{
        padding-left: 6px;
        margin: 0;
        border: none;
    }}

    QGroupBox QLineEdit, 
    QGroupBox QComboBox {{
        background-color: {QTMATERIAL_SECONDARYDARKCOLOR};
    }}

    QPushButton.comboHeightButton {{
        height: 27px;
        min-height: 27px;
        max-height: 27px;
    }}

    QGroupBox QListWidget {{
        background-color: {QTMATERIAL_SECONDARYDARKCOLOR};
        margin-top: 15px;
        margin-bottom: 5px;
        /*padding-left: 25px;*/
    }}

    QLineEdit[readOnly="true"] {{
        background-color: #2b2f33;
    }}

    QPushButton:flat, 
    QPushButton:flat:hover, 
    QPushButton:flat:pressed, 
    QPushButton:flat:checked, 
    QPushButton:flat:disabled {{
        padding: 0px;
        border: none;
        background-color: transparent;
    }}

    QPushButton:flat:hover {{
        color: {QTMATERIAL_SECONDARYTEXTCOLOR}
    }}

    QDialog QToolButton,
    QDialog QToolButton:hover,
    QDialog QToolButton:pressed,
    QDialog QToolButton:checked {{
        background-color: transparent;
        border: none;
        opacity: 0.8;
    }}
    QDialog QToolButton:hover {{
        opacity: 1;
    }}

    QMenu {{
        border: none;
        margin: 0px;
    }}

    QStatusBar {{
        font-size: 12px;
        color: {QTMATERIAL_SECONDARYTEXTCOLOR};
    }}

    QGroupBox QLineEdit:disabled,
    QGroupBox QComboBox:disabled,
    QGroupBox QPlainTextEdit:disabled {{
        background-color: #2b2f33;
        color: #858585;
        border-radius: 4px;
        border: none;
    }}

    QMessageBox QPushButton {{
        height: 23px;
        min-height: 23px;
        max-height: 23px;
    }}

    .secondaryBg {{
        background-color: {QTMATERIAL_SECONDARYCOLOR};
    }}

    .squareTop {{
        border-top-right-radius: 0px;
        border-top-left-radius: 0px;
    }}

    .squareBottom {{
        border-bottom-right-radius: 0px;
        border-bottom-left-radius: 0px;
    }}

    .transparent {{
        background-color: transparent;
    }}

    .dim {{
        color: #858585;
    }}

"""