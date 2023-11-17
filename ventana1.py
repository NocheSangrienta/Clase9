import sys

from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton


class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1, self). __init__(parent)

        self.setWindowTitle("Formulario de registro")

        # Poner el icono
        self.setWindowIcon(QtGui.QIcon('imagenes/icono.png'))

        # Establecer el ancho y el alto
        self.ancho = 900
        self.alto = 600

        # Estableciendo el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Hacer que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Fijar el ancho y el alto de la ventana:
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Establecemos el fondo principal
        self.fondo = QLabel(self)

        # definios la imagen de fondo:
        self.imagenFondo = QPixmap('imagenes/imagen3.jpg')

        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imgane:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Estblecemos la distribucion de los elemntos en layout horizontl:
        self.horizontal = QVBoxLayout()

        # le ponemos los margenes:
        self.horizontal.setContentsMargins(30,30,30,30)

        #-------------------LAYOUT IZQUIERDO-------------------------

        self.ladoIzquierdo = QFormLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Hacemos el letrero
        self.letrero1.setText("Informacion del Cliente")

        # Le asignamos tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto y margenes
        self.letrero1.setStyleSheet("color: #000000;")

        # Agregamos el letrero en la primera fila:
        self.ladoIzquierdo.addRow(self.letrero1)

        # Hacemoe el letrero:
        self.letrero2 = QLabel()

        # Establecemos el ancho del label:
        self.letrero2.setFixedWidth(340)

        # Le escribimos el texto:
        self.letrero2.setText("Por favor ingrese la informacion del cliente"
                              "\nen el formulario de abajo. Los campos marcados "
                              "\ncon asterisco son obligatorios.")

        # Le escribimos el texto
        self.letrero2.setFont(QFont("Andale Mono", 10))

        # Le ponemos color de texto y margenes:
        self.letrero2.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la fila siguiente:
        self.ladoIzquierdo.addRow(self.letrero2)


        # Hacemos el campo para ingresar el password:
        self.nombreCompleto = QLineEdit()
        self.nombreCompleto.setFixedWidth(250)


        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Nombre completo*", self.nombreCompleto)

        # Hacemos el campò para ingresar el usuario:
        self.usuario = QLineEdit()
        self.usuario.setFixedWidth(250)

        # Agregamos estos al formulario:
        self.ladoIzquierdo.addRow("Usuario*", self.usuario)

        # Hacemos el campo para ingresar el password:
        self.password = QLineEdit()
        self.password.setFixedWidth(250)
        self.password.setEchoMode(QLineEdit.Password)

        # Agregamos el layout ladoIzquierdo al layout horizontal:
        self.ladoIzquierdo.addRow("Password*", self.password)

        # Hacemos el campo para ingresar el password:
        self.password2 = QLineEdit()
        self.password2.setFixedWidth(250)
        self.password2.setEchoMode(QLineEdit.Password)

        # Agregamos estos en el formulario:
        self.ladoIzquierdo.addRow("Password*", self.password2)

        # Hacemos el campo ingresar el documento:
        self.documento = QLineEdit()
        self.documento.setFixedWidth(250)

        # Agregamos el documento en el formulario:
        self.ladoIzquierdo.addRow("Documento*", self.documento)

        # Hacemos el campo para ingresar el correo:
        self.correo = QLineEdit()
        self.correo.setFixedWidth(250)

        # Hacemos el campo para ingresar el correo:
        self.ladoIzquierdo.addRow("Correo*", self.correo)

        # Hacemos el boton para registrar los datos:
        self.botonRegistrar = QPushButton("Registrar")

        # Establecemos el ancho del boton:
        self.botonRegistrar.setFixedWidth(90)

        #  Le ponemos los estilos:
        self.botonRegistrar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")


        self.botonRegistrar.clicked.connect(self.accion_botonRegistrar)

        # Hacemos el boton para limpiar los datos:
        self.botonLimpiar = QPushButton("limpiar")

        # Establecemos el ancho del boton:
        self.botonLimpiar.setFixedWidth(90)

        #  Le ponemos los estilos:
        self.botonLimpiar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding: 10px;"
                                          "margin-top: 40px;")

        self.botonLimpiar.clicked.connect(self.accion_botonLimpiar)

        # Agregamos los dos botones al laayout ladoIzquierdo:
        self.ladoIzquierdo.addRow(self.botonRegistrar, self.botonLimpiar)


        # Agregamos el Layout ladoizquierdo al layout horizontal:
        self.horizontal.addLayout(self.ladoIzquierdo)

        # ----------------OJOO IMPORTANTE PONER AL FINAL-----------------

        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)

    # Metodo del botonLimpiar
    def accion_botonLimpiar(self):
        pass



    # Metodo del botonRegistar
    def accion_botonRegistrar(self):
        pass






if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())















