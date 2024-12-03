STYLE_SHEET = """
    QLabel#label_title {
        font-weight: bold;
        font-size: 20px;
        color: rgb(2, 102, 0);
    }

    QLabel#label_card {
        font-weight: bold;
        font-size: 14px;
    }

    QWidget#widget_login {
        background-color: rgb(255, 255, 128);
    }

    QWidget#widget_nav {
        background-color: rgb(255, 255, 102);
    }

    QWidget#widget_card:hover {
        background-color: rgb(230, 230, 0);
        border-top: 2px solid rgb(2, 102, 0);
    }

    QWidget#widget_card_pressed {
        background-color: rgb(230, 230, 0);
        border-top: 2px solid rgb(2, 102, 0);
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

    QLabel#label_button {
        font-weight: bold;
        color: rgb(0, 123, 255);
    }

    QLabel#label_button:hover {
        font-weight: bold;
        color: rgb(0, 99, 204);
    }

    QScrollArea#n_page {
        background-color: rgb(255, 0, 0);
    }
    QScrollArea#m_page {
        background-color: rgb(0, 255, 0);
    }
    QScrollArea#h_page {
        background-color: rgb(0, 0, 255);
    }
"""