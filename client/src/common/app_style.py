STYLE_SHEET = """
    QLabel#label_title {
        font-weight: bold;
        font-size: 20px;
        color: rgb(2, 102, 0);
    }

    QLabel#label_prompt {
        font-weight: bold;
        font-size: 16px;
    }

    QLabel#label_sidebar_button {
        font-weight: bold;
        font-size: 16px;
    }

    QLabel#label_username {
        font-weight: bold;
        font-size: 18px;
    }

    QLabel#label_button {
        font-size: 14px;
        font-weight: bold;
        color: rgb(0, 123, 255);
    }

    QLabel#label_button:hover {
        font-size: 14px;
        font-weight: bold;
        color: rgb(0, 99, 204);
    }

    QWidget#widget_component {
        background-color: rgb(255, 255, 102);
    }

    QWidget#widget_modal {
        background-color: rgb(255, 255, 102);
        border-radius: 15px;
    }

    QWidget#widget_button:hover {
        background-color: rgb(230, 230, 0);
        border-top: 2px solid rgb(2, 102, 0);
    }

    QWidget#widget_button_pressed {
        background-color: rgb(230, 230, 0);
        border-top: 2px solid rgb(2, 102, 0);
    }

    QWidget#widget_sidebar_button:hover {
        background-color: rgb(230, 230, 0);
        border-left: 2px solid rgb(2, 102, 0);
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