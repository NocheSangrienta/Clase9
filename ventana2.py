
import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QLabel, QVBoxLayout, QApplication, QDesktopWidget, QScrollArea, QWidget, \
    QGridLayout, QButtonGroup, QPushButton
from PyQt5 import QtGui

import math

from cliente import Cliente
from ventana3 import Ventana3


class Ventana2(QMainWindow):
    def __init__(self, anterior):
        super(Ventana2, self).__init__(anterior)

        #Creamos un atributo que guarde la ventana anterior:
        self.ventanaAnterior = anterior

        self.setWindowTitle("Usuarios registrados")

        # Poner el iciono
        self.setWindowIcon(QtGui.QIcon("imagenes/ojo.jpg"))

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
        self.imagenFondo = QPixmap('imagenes/rio.jpg')

        self.fondo.setPixmap(self.imagenFondo)

        # Establecemos el modo para escalar la imagen
        self.fondo.setScaledContents(True)

        # Hacemos que se adapte el tamaño de la imgane:
        self.resize(self.imagenFondo.width(), self.imagenFondo.height())

        # Establecemos la ventana de fondo como la ventana central
        self.setCentralWidget(self.fondo)

        # Estblecemos la distribucion de los elemntos en layout horizontl:
        self.vertical = QVBoxLayout()

        # Hacemos el titulo
        self.letrero1 = QLabel()

        # Hacemos el letrero
        self.letrero1.setText("Usuarios Registrados")

        # Le asignamos tipo de letra:
        self.letrero1.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto y margenes
        self.letrero1.setStyleSheet("color: #000080;")

        # Agregamos el letrero en la primera fila:
        self.vertical.addWidget(self.letrero1)

        # Ponemos un espacio despues:
        self.vertical.addStretch()

        # Creamos un sccroll:
        self.scrollArea = QScrollArea()

        # Le ponemos  trasparente el fondo del scroll:
        self.scrollArea.setStyleSheet("background-color: transparent;")

        # Hacemos que el scroll se adapte a diferentes tamaños:
        self.scrollArea.setWidgetResizable(True)

        # Creamos una ventana contenedora para cada celda:
        self.contenedora = QWidget()

        # vAMOS A crear un layout de grid para poner una cuadricula de elementos:
        self.cuadricula = QGridLayout(self.contenedora)

        # Metemos la ventana contenedora en el scroll
        self.scrollArea.setWidget(self.contenedora)

        # Metemos en el layout vertical el scroll:
        self.vertical.addWidget(self.scrollArea)

        # Abrimos el archivo en modo de lectura:
        self.file = open('datos/clientes.txt', 'rb')

         # crear lista vacia
        self.usuarios = []

        # Recorremos el archivo, linea por linea:
        while self.file:
            linea = self.file.readline().decode('UTF-8')
            # Obtenemos del string una lista con 11 datos separados por:
            lista = linea.split(";")
            # se para si ya no hay mas registros en el archivo
            if linea == '':
                break

            # Creamos un objeto tipo cliente llamado u
            u = Cliente(
                lista[0],
                lista[1],
                lista[2],
                lista[3],
                lista[4],
                lista[5],
                lista[6],
                lista[7],
                lista[8],
                lista[9],
                lista[10],
            )

            # Metemos el  objeto en la lista de usuarios:
            self.usuarios.append(u)

        # Cerramos el archivo
        self.file.close()

        # En este punto tenemos la lista usuarios con todos los usuarios

        # Obtenemos el numero de usuarios registrados:
        # Consultamos el tamaño de la lista usuarios:
        self.numeroUsuarios = len(self.usuarios)

        # Contador de elementos para controlar a los usuarios en la lista usuarios:
        self.contador = 0

        # Definimos la cantidad de elementos para mostrar por columna
        self.elementosPorColumna = 3

        # CCalculamos el numero de filas
        # Redondeamos el entero superior + 1 dividimos por elementosPorColumna:
        self.numeroFilas = math.ceil(self.numeroUsuarios / self.elementosPorColumna) + 1

        # Controlamos todos los botones por una variable
        self.botones = QButtonGroup()

        # Definimos que el controlador de los botones
        # Debe agruparse a todos los botones internos
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):

                # validamos que se estan ingresando la cantidad de usuarios correcta:
                if self.contador < self.numeroUsuarios:

                    # EN cada celda de la cuadricula va una ventana:
                    self.ventanaAuxiliar = QWidget()

                    # se determina su alto y su ancho:
                    self.ventanaAuxiliar.setFixedHeight(100)
                    self.ventanaAuxiliar.setFixedWidth(200)

                    # Ceamos un layout vertical para cada elemento de la Cuadricula:
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un boton por cada usuario mostrando su ccedula:
                    self.botonAccion = QPushButton(self.usuarios[self.contador].documento)

                    self.botonAccion.setFixedWidth(150)

                    self.botonAccion.setStyleSheet("background-color: #008B45;"
                                                   "color: #FFFFFF;"
                                                   "padding: 10px;"
                                                   )

                    # Metemos el boton en el layout vertical para que se vea:
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo, con su cedula como id:
                    self.botones.addButton(self.botonAccion, int(self.usuarios[self.contador].documento))

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # Ala ventana le asignamos el layout vertical:
                    self.ventanaAuxiliar.setLayout(self.verticalCuadricula)

                    # A la cuadricula le agregamos la ventana en la fila y columna actual:
                    self.cuadricula.addWidget(self.ventanaAuxiliar, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1

        # Establecemos el metodo para que funcionen todos los botones
        self.botones.idClicked.connect(self.metodo_accionBotones)

             #-----------botonFormaTabular-------------------

        # Hacemos el boton para tabular ala entna anterios
        self.botonFormaTabular = QPushButton("Forma Tabular")

        # Estableceos el ancho
        self.botonFormaTabular.setFixedWidth(100)

        self.botonFormaTabular.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )

        #Hacemos que el boton botonFormaTabular tengga s metodo
        self.botonFormaTabular.clicked.accion(self.metodo_botonFormaTabular)

        self.vertical.addWidget(self.botonFormaTabular)


        # --------------BotonVolver----------------

        # Hacemos el boton para devolvernos a la ventana anterior:
        self.botonVolver = QPushButton("Volver")

        # Establecemos el ancho del boton
        self.botonVolver.setFixedWidth(90)

        # Le ponemos estilos
        self.botonVolver.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;"
                                       )

        # Hacemos que el boton tenga su metodo
        self.botonVolver.clicked.connect(self.metodo_botonVolver)

        #  Metemos el layout en el botonVolver
        self.vertical.addWidget(self.botonVolver)

        # ----------------OJOO IMPORTANTE PONER AL FINAL-----------------

        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.vertical)

    def metodo_accionBotones(self, cedulaUsuario):
        print(cedulaUsuario)

    def metodo_botonVolver(self):
        self.hide()
        self.ventana3 = Ventana3(self)
        self.ventana3.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)

    ventana2 = Ventana2()

    ventana2.show()

    sys.exit(app.exec_())