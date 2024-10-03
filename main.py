from PyQt5 import uic, QtWidgets
from colorama import Cursor
import mysql.connector

MIN_PASSWORD_LENGTH = 8

def show_login_screen():
    initial_screen.close()
    login_screen.show()
    login_screen.label_2.setText("")

def show_register_screen():
    initial_screen.close()
    register_screen.show()
    register_screen.label_6.setText("")
    register_screen.label_7.setText("")

def login():
    username = login_screen.lineEdit_login.text()
    password = login_screen.lineEdit_password.text()

    try:
        db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
        cursor = db_connection.cursor()
        cursor.execute("SELECT password FROM login WHERE username = %s", (username,))
        stored_password = cursor.fetchone()[0]
        db_connection.close()

        if password == stored_password:
            login_screen.lineEdit_login.setText("")
            login_screen.lineEdit_password.setText("")
            login_screen.close()
            main_screen.show()
            main_screen.label_User.setText(username)
        else:
            login_screen.label_2.setText("Incorrect login details!")
            print("Incorrect login details!")

    except Exception as e:
        print("Error during login: ", e)
        login_screen.label_2.setText("Error during login")

def back_to_login_screen():
    login_screen.close()
    initial_screen.show()

def register():
    email = register_screen.lineEdit_email.text()
    username = register_screen.lineEdit_username.text()
    password = register_screen.lineEdit_password.text()
    confirm_password = register_screen.lineEdit_password2.text()

    if len(password) >= MIN_PASSWORD_LENGTH:
        if password == confirm_password:
            db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
            cursor = db_connection.cursor()
            insert_query = ("INSERT INTO login (email, username, password) VALUES (%s, %s, %s)")
            data = (email, username, password)
            cursor.execute(insert_query, data)
            db_connection.commit()
            db_connection.close()
            register_screen.lineEdit_email.setText("")
            register_screen.lineEdit_username.setText("")
            register_screen.lineEdit_password.setText("")
            register_screen.lineEdit_password2.setText("")
            register_screen.label_6.setText("")
            register_screen.label_7.setText("Successfully registered!")
            print("Successfully registered!")
        else:
            register_screen.label_6.setText("Passwords do not match!")
            print("Passwords do not match!")
    else:
        register_screen.label_6.setText("Password must be at least 8 characters long!")
        register_screen.label_7.setText("")
        print("Password must be at least 8 characters long!")

def back_to_register_screen():
    register_screen.close()
    initial_screen.show()

def back_to_main_screen():
    main_screen.close()
    initial_screen.show()

app = QtWidgets.QApplication([])
initial_screen = uic.loadUi(r"initial_screen.ui")
login_screen = uic.loadUi(r"login_screen.ui")
register_screen = uic.loadUi(r"register_screen.ui")
main_screen = uic.loadUi(r"main_screen.ui")

initial_screen.pushButton.clicked.connect(show_login_screen)
initial_screen.pushButton_2.clicked.connect(show_register_screen)

login_screen.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
login_screen.pushButton.clicked.connect(login)
login_screen.pushButton_back.clicked.connect(back_to_login_screen)

register_screen.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
register_screen.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Password)
register_screen.pushButton.clicked.connect(register)
register_screen.pushButton_back.clicked.connect(back_to_register_screen)

main_screen.pushButton.clicked.connect(back_to_main_screen)

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
cursor = db_connection.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS login (
        id INT NOT NULL AUTO_INCREMENT,
        email VARCHAR(110) NOT NULL,
        username VARCHAR(45) NOT NULL,
        password VARCHAR(45) NOT NULL,
        birth_date DATE NULL,
        PRIMARY KEY (id)
    ) DEFAULT CHARACTER SET = utf8mb4;
""")
db_connection.commit()
db_connection.close()

initial_screen.show()
app.exec()
