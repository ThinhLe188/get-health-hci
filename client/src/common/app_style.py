STYLE_SHEET = """
    QLabel#label_title {
        font-weight: bold;
        font-size: 16px;
        color: rgb(2, 102, 0);
    }

    QLabel#label_card {
        font-weight: bold;
        font-size: 14px;
    }

    QWidget#widget_nav {
        background-color: rgb(255, 255, 153);
        border: 1px solid black;
    }

    QWidget#widget_card:hover {
        background-color: rgb(255, 255, 128);
        border: 1px solid black;
    }
     
    QLineEdit#input_prompt {
        padding: 4px;
        border: 1px solid #cccccc;
        border-radius: 5px;
        font-size: 14px;
    }

    QLineEdit#input_prompt:focus {
        border-color: #0078d7;
        outline: none;
    }

    QPushButton#button_submit {
        background-color: rgb(3, 153, 0);
        border-radius: 5px;
        padding: 10px;
        font-weight: bold;
        font-size: 16px;
        color: white;
    }

    QPushButton#button_submit:hover {
        background-color: rgb(2, 128, 0);
    }
"""