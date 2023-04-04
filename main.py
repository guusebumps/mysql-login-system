from PyQt5 import  uic,QtWidgets
from colorama import Cursor
import mysql.connector

# Constantes
caracteres_min_senha = 8

# Tela inicial
def chama_tela_login():
    tela_inicial.close()
    tela_login.show()
    tela_login.label_2.setText("")

def chama_tela_cadastro():
    tela_inicial.close()
    tela_cadastro.show()
    tela_cadastro.label_6.setText("")
    tela_cadastro.label_7.setText("")

# Tela de login
def login():
    nome_usuario = tela_login.lineEdit_login.text()
    senha = tela_login.lineEdit_senha.text()

    try:
        banco_login = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
        cursor = banco_login.cursor()
        cursor.execute("SELECT password FROM login WHERE username = '{}'".format(nome_usuario))
        # cursor.execute("SELECT AES_DECRYPT(password,'senhadachave') AS password FROM login WHERE username = '{}'".format(nome_usuario))
        # # cursor.execute("SELECT CAST(AES_DECRYPT(password,'senhadachave') as char) FROM login WHERE username = '{}'".format(nome_usuario))
        senha_bd = cursor.fetchone()[0]
        banco_login.close()

        if senha == senha_bd:
            tela_login.lineEdit_login.setText("")
            tela_login.lineEdit_senha.setText("")
            tela_login.close()
            tela_principal.show()
            tela_principal.label_User.setText(nome_usuario)
        else:
            tela_login.label_2.setText("Dados de login incorretos!")
            print("Dados de login incorretos!")

    except Exception as e:
        print("Erro ao fazer login: ", e)
        tela_login.label_2.setText("Erro ao fazer login")

def volta_tela_login():
    tela_login.close()
    tela_inicial.show()

# Tela de cadastro
def cadastrar():
    email_cadastrado = tela_cadastro.lineEdit_email.text()
    usuario_cadastrado = tela_cadastro.lineEdit_username.text()
    senha_cadastrada = tela_cadastro.lineEdit_password.text()
    confirma_senha = tela_cadastro.lineEdit_password2.text()    

    if len(senha_cadastrada) >= caracteres_min_senha:

        if senha_cadastrada == confirma_senha:

            banco_cadastro = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
            cursor = banco_cadastro.cursor()
            comando_SQL_cadastro = ("INSERT INTO login (`e-mail`,username,password) VALUES (%s,%s,%s)")
            # comando_SQL_cadastro = ("INSERT INTO login (`e-mail`,username,password) VALUES (%s,%s,AES_ENCRYPT(%s, 'senhadachave'))")
            dados_cadastro = (str(email_cadastrado),str(usuario_cadastrado),str(senha_cadastrada))
            cursor.execute(comando_SQL_cadastro,dados_cadastro)
            banco_cadastro.commit()
            banco_cadastro.close()
            tela_cadastro.lineEdit_email.setText("")
            tela_cadastro.lineEdit_username.setText("")
            tela_cadastro.lineEdit_password.setText("")
            tela_cadastro.lineEdit_password2.setText("")
            tela_cadastro.label_6.setText("")
            tela_cadastro.label_7.setText("Cadastrado com sucesso!")
            print("Cadastrado com sucesso!")
        else:
            tela_cadastro.label_6.setText("As senhas não coincidem!")
            print("As senhas não coincidem!")
    else:
        tela_cadastro.label_6.setText("Sua senha deve possuir mais de 8 dígitos!")
        tela_cadastro.label_7.setText("")
        print("Sua senha deve possuir mais de 8 dígitos!")

def volta_tela_cadastro():
    tela_cadastro.close()
    tela_inicial.show()

# Tela principal
def volta_tela_principal():
    tela_principal.close()
    tela_inicial.show()

app=QtWidgets.QApplication([])
tela_inicial=uic.loadUi(r"tela_inicial.ui")
tela_login=uic.loadUi(r"tela_login.ui")
tela_cadastro=uic.loadUi(r"tela_cadastro.ui")
tela_principal=uic.loadUi(r"tela_final.ui")

tela_inicial.pushButton.clicked.connect(chama_tela_login)
tela_inicial.pushButton_2.clicked.connect(chama_tela_cadastro)

tela_login.lineEdit_senha.setEchoMode(QtWidgets.QLineEdit.Password)
tela_login.pushButton.clicked.connect(login)
tela_login.pushButton_voltar.clicked.connect(volta_tela_login)

tela_cadastro.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.lineEdit_password2.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro.pushButton.clicked.connect(cadastrar)
tela_cadastro.pushButton_2.clicked.connect(volta_tela_cadastro)

tela_principal.pushButton.clicked.connect(volta_tela_principal)

# Abre o Banco de Dados e Cria Tabela
banco_create_table = mysql.connector.connect(host="localhost", user="root", passwd="", database="login")
cursor = banco_create_table.cursor()
cursor.execute("CREATE TABLE if not exists login (id INT NOT NULL AUTO_INCREMENT,  email VARCHAR(110) NOT NULL,  email VARCHAR(110) NOT NULL,  username VARCHAR(45) NOT NULL,  password VARCHAR(45) NOT NULL,  data_nascimento DATE NULL,  PRIMARY KEY (id))DEFAULT CHARACTER SET = utf8mb4;")
banco_create_table.commit()
banco_create_table.close()

tela_inicial.show()
app.exec()