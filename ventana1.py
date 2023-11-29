import sys


from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QLabel, QVBoxLayout, QApplication, QFormLayout, QLineEdit, \
    QPushButton, QHBoxLayout, QDialog, QDialogButtonBox
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from cliente import Cliente
from ventana2 import Ventana2

class Ventana1(QMainWindow):

    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent)

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
        self.horizontal = QHBoxLayout()

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
        self.letrero1.setStyleSheet("color: #000080;")

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


        #---------------------------LAYOUT DERECHO-----------------------

        # Creamos el layout del lado Derecho:
        self.ladoDerecho = QFormLayout()

        # Se le asigna la margen solo ala izquierda de 100px:
        self.ladoDerecho.setContentsMargins(100, 0, 0, 0)

        # Hacemos el letrero:
        self.letrero3 = QLabel()

        # Le escribimos el texto:
        self.letrero3.setText("Recuperar Contraseña")

        # Le asignamos el tipo de letra:
        self.letrero3.setFont(QFont("Andale Mono", 20))

        # Le ponemos color de texto:
        self.letrero3.setStyleSheet("color: #000080;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero3)

        # Hacemos el letrero:
        self.letrero4 = QLabel()

        # Establecemos el ancho del label:
        self.letrero4.setFixedWidth(400)

        self.letrero4.setText("Por favor ingrese la informacion para recuperar "
                              "\nla contraseña. los campos marcados"
                              "\ncon asterisco son obligatorios.")

        # Le escribimos el texto:
        self.letrero4.setStyleSheet("color: #000080; margin-bottom: 40px;"
                                    "margin-top: 20px;"
                                    "padding-bottom: 10px;"
                                    "border: 2px solid #000080;"
                                    "border-left: none;"
                                    "border-right: none;"
                                    "border-top: none;")

        # Agregamos el letrero en la primera fila:
        self.ladoDerecho.addRow(self.letrero4)

        # ----1

        # Hacemos el letrero de la pregunta 1:
        self.labelPregunta1 = QLabel("Pregunta de verificacion 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta1)

        # Hacemos el campo para ingresar la pregunta 1:
        self.pregunta1 = QLineEdit()
        self.pregunta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta1)

        # Hacemos el letrero de la respesta 1:
        self.labelRespuesta1 = QLabel("Respuesta de verificacion 1*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta1)

        # Hacemos el campo para ingresar la respuesta 1:
        self.respuesta1 = QLineEdit()
        self.respuesta1.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta1)

        # -----2

        # Hacemos el letrero de la pregunta 2:
        self.labelPregunta2 = QLabel("Pregunta de verificacion 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta2)

        # Hacemos el campo para ingresar la pregunta 2:
        self.pregunta2 = QLineEdit()
        self.pregunta2.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta2)

        # Hacemos el letrero de la respesta 1:
        self.labelRespuesta2 = QLabel("Respuesta de verificacion 2*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta2)

        # Hacemos el campo para ingresar la respuesta 2:
        self.respuesta2= QLineEdit()
        self.respuesta2.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta2)

        #-----3

        # Hacemos el letrero de la pregunta 3:
        self.labelPregunta3 = QLabel("Pregunta de verificacion 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelPregunta3)

        # Hacemos el campo para ingresar la pregunta 3:
        self.pregunta3 = QLineEdit()
        self.pregunta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.pregunta3)

        # Hacemos el letrero de la respesta 3:
        self.labelRespuesta3 = QLabel("Respuesta de verificacion 3*")

        # Agregamos el letrero en la fila siguiente:
        self.ladoDerecho.addRow(self.labelRespuesta3)

        # Hacemos el campo para ingresar la respuesta 3:
        self.respuesta3 = QLineEdit()
        self.respuesta3.setFixedWidth(320)

        # Agregamos el campo en el formulario:
        self.ladoDerecho.addRow(self.respuesta3)

        # Hacemos el boton para buscar las preguntas:
        self.botonBuscar = QPushButton("Buscar")

        # Establecemos el ancho del boton:
        self.botonBuscar.setFixedWidth(90)

        # Establecemos el ancho del boton:
        self.botonBuscar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;")

        self.botonBuscar.clicked.connect(self.accion_botonBuscar)

        # Hacemos el boton para recuperar la contraseña:
        self.botonRecuperar = QPushButton("Recuperar")

        # Establecemos el ancho del boton:
        self.botonRecuperar.setFixedWidth(90)

        # Establecemos el ancho del boton:
        self.botonRecuperar.setStyleSheet("background-color: #008B45;"
                                       "color: #FFFFFF;"
                                       "padding: 10px;"
                                       "margin-top: 10px;")

        self.botonRecuperar.clicked.connect(self.accion_botonRecuperar)


        # Agregamos los botones al layout ladoDerecho:
        self.ladoDerecho.addRow(self.botonBuscar, self.botonRecuperar)

        # --------Boton Continuar---------
        # Hacemos el boton para pasar ala siguiente ventana:
        self.botonContinuar = QPushButton("Continuar")

        self.botonContinuar.setFixedWidth(90)
        self.botonContinuar.setStyleSheet("background-color: #008B45;"
                                          "color: #FFFFFF;"
                                          "padding:10px;"
                                          "margin-top: 10px;"
                                          )

        # Hacemos que el botonContinuar tenga su metodo
        self.botonContinuar.clicked.connect(self.accion_botonContinuar)

        # Agregamos el botonContinuar al layoutDerecho:
        self.ladoDerecho.addRow(self.botonContinuar)



        # Agregamos el layout ladoDerecho al layout horizontal:
        self.horizontal.addLayout(self.ladoDerecho)

        # ----------------OJOO IMPORTANTE PONER AL FINAL-----------------

        # Indicamos que el layout principal del fondo es horizontal:
        self.fondo.setLayout(self.horizontal)


        # Creamos la ventana de dialogo:
        self.ventanaDialogo = QDialog(None, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Definimos el tamaño de la ventana:
        self.ventanaDialogo.resize(300, 150)

        # Creamos el boton para aceptar:
        self.botonAceptar = QDialogButtonBox.Ok
        self.opciones = QDialogButtonBox(self.botonAceptar)
        self.opciones.accepted.connect(self.ventanaDialogo.accept)

        # Estaqblecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Formulario de registro")

        # Configuramos la ventana para que sea modal:
        self.ventanaDialogo.setWindowModality(Qt.ApplicationModal)

        # Creamos un layout vertical
        self.vertical = QVBoxLayout()

        # Creamos un label para los mensajes:
        self.mensaje = QLabel("Debe ingresar todos los campos")

        # Le ponemos estilos al label mensaje:
        self.mensaje.setStyleSheet("background-color: #008B45; color: #FFFFFF; padding: 10px;")

        # Agregamos el label de mensaje
        self.vertical.addWidget(self.mensaje)

        # Agregamos las opciones de los botones:
        self.vertical.addWidget(self.opciones)

        # Establecemos el layout para la ventana:
        self.ventanaDialogo.setLayout(self.vertical)



    # Metodo del botonLimpiar
    def accion_botonLimpiar(self):
        self.nombreCompleto.setText("")
        self.usuario.setText("")
        self.password.setText("")
        self.password2.setText("")
        self.documento.setText("")
        self.correo.setText("")
        self.pregunta1.setText("")
        self.respuesta1.setText("")
        self.pregunta2.setText("")
        self.respuesta2.setText("")
        self.pregunta3.setText("")
        self.respuesta3.setText("")







    # Metodo del botonRegistar
    def accion_botonRegistrar(self):
        # variable para controlar que se han ingresado los datos correctos:
        self.datoscorrectos = True



        # Validamos que los dos passwords sean iguales
        if (
                self.password.text() != self.password2.text()
        ):
            self.datoscorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Los passwprds no son iguales")

            # Hacemos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

            # Validamos que se ingresen todos los campos
        if (
                self.nombreCompleto.text() == ''
                or self.usuario.text() == ''
                or self.password.text() == ''
                or self.documento.text() == ''
                or self.correo.text() == ''
                or self.pregunta1.text() == ''
                or self.respuesta1.text() == ''
                or self.pregunta2.text() == ''
                or self.respuesta2.text() == ''
                or self.pregunta3.text() == ''
                or self.respuesta3.text() == ''
        ):
            self.datoscorrectos = False

            self.mensaje.setText("Debe ingresar todos los campos")

            # Escribimos que la ventana de dialogo se vea:
            self.ventanaDialogo.exec_()

        # Si los datos estan correctos:
        if self.datoscorrectos:

            # Abrimos el archivo en modo agregar escribiendo datos en binario.
            self.file = open('datos/clientes.txt', 'ab')

            # Traer los textos de los QLineEdit() y los agrega concatenandolos
            # Para escribirlos en el archivo en formato binario utf-8
            self.file.write(bytes(
                self.nombreCompleto.text() + ";"
                + self.usuario.text() + ";"
                + self.password.text() + ";"
                + self.password2.text() + ";"
                + self.documento.text() + ";"
                + self.correo.text() + ";"
                + self.pregunta1.text() + ";"
                + self.respuesta1.text() + ";"
                + self.pregunta2.text() + ";"
                + self.respuesta2.text() + ";"
                + self.pregunta3.text() + ";"
                + self.respuesta3.text() + "\n"
                ,encoding='UTF-8'))

            # Cerramos el archivo
            self.file.close()




            # Abrimos en modo de lectura en formato bytes
            self.file = open('datos/clientes.txt', 'rb')
            # Recorrer el archivo linea por linea.
            while self.file:
                linea = self.file.readline().decode('UTF-8')
                print(linea)
                if linea == '': # Para cuando encuentre una linea vacia
                    break
            self.file.close()

    # Metodo del botonBuscar:
    def accion_botonBuscar(self):
        # variable para controlar que se han ingresado los datos correctos:
        self.datoscorrectos = True

        # Establecemos  el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Buscar preguntas de validacion")

        # validar que se haya ingresado el documento:
        if (
            self.documento.text() == ''
        ):
            self.datoscorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("si va a buscar preguntas"
                                 "para recuperar la contraseña."
                                 "\nDebe primero, ingresar el documento.")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()
        # Validar si el documento es numerico:
        if (
            not self.documento.text().isnumeric()
        ):
            self.datoscorrectos = False

            # Escribimos el texto explicativo
            self.mensaje.setText("El documento debe ser numerico."
                                 "\nNo ingrese letras"
                                 "ni caracteres especiales.")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()

            # Limpiamos el campo del documento
            self.documento.setText('')

        if (
            self.datoscorrectos

        ):
            #Abrimos el archivvo en modo lectura:
            self.file = open('datos/clientes.txt', 'rb')

            # lista vacia para guardar todos los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # Obtenemos del string una lista con 11 datos separados por:
                lista = linea.split(";")

                # Se para si ya no hay mas registros en el archivo
                if linea == '':
                    break

                # Creamos un objeto tipo cliente llamdo U

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

                # Metemos el objeto en la lista de usuarios
                usuarios.append(u)
            # cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista usuarios con todos los usuarios:
            existeDocumento = False

            # Buscamosen la lista usuario por usuario si existe la cedula:
            for u in usuarios:
                # Comparamos el documento ingresado:
                # si corresponde con el documento, es el usuario correcto:
                if u.documento == self.documento.text():
                    # Mostramos las preguntas en el formulario
                    self.pregunta1.setText(u.pregunta1)
                    self.pregunta2.setText(u.pregunta2)
                    self.pregunta3.setText(u.pregunta3)

                    # indicamos que encontramos el documento
                    existeDocumento = True

                    # Paramos el for:
                    break
            # Si no existe un usuario con este documento:
            if (
                     not existeDocumento
            ):
                # Esribimos el texto explicativo:
                self.mensaje.setText("No existe un usuario con este documento:\n"
                                     + self.documento.text())

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()
    # Metodo del botonRecuperar
    def accion_botonRecuperar(self):
        # Variable para controlar que se han ingresado los datos correctos:
        self.datoscorrectos = True

        # Establecemos el titulo de la ventana:
        self.ventanaDialogo.setWindowTitle("Recuperar contraseña")

        # Validamos que se hayan buscado las preguntas:
        if (
                self.pregunta1.text() == '' or
                self.pregunta2.text() == '' or
                self.pregunta3.text() == ''
        ):
            self.datoscorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "\nbuscar las preguntas de verificacion."
                                 "\n\nPrimero ingrese su documento y luego"
                                 "\npresione el boton 'Buscar'")

            # Hacemos que la ventana de dialogo se muestre
            self.ventanaDialogo.exec_()
        # Validamos si se buscaron las preguntas pero no se ingresaron las respuestas:
        if (
                self.pregunta1.text() != '' and
                self.respuesta1.text() == '' and
                self.pregunta2.text() != '' and
                self.respuesta2.text() == '' and
                self.pregunta3.text() != '' and
                self.respuesta3.text() == ''

        ):
            self.datoscorrectos = False

            # Escribimos el texto explicativo:
            self.mensaje.setText("Para recuperar la contraseña debe"
                                 "\ningresar las respuestas a cada pregunta.")

            # Hacemos que la ventana de dialogo se vea
            self.ventanaDialogo.exec_()
        #si los datos son correctos:
        if (
                self.datoscorrectos
        ):
            # Abrimos el archivo en modo de lectura:
            self.file = open('datos/clienteS.txt', 'rb')

            # Lista vacia para guarda los usuarios:
            usuarios = []

            while self.file:
                linea = self.file.readline().decode('UTF-8')
                # Obtenemos del string una lista con 11 datos separados por:
                lista = linea.split(";")

                # Se para si ya no hay mas registros en el archivo
                if linea == '':
                    break

                # Creamos un objeto tipo cliente llamdo U

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

                # Metemos el objeto en la lista de usuarios
                usuarios.append(u)

            # cerramos el archivo:
            self.file.close()

            # En este punto tenemos la lista usuarios con todos los usuarios:

            # Variable para controlar si existe el documento:
            existeDocumento = False

            # Definimos las variables para guardar las preguntas:
            resp1 = ''
            resp2 = ''
            resp3 = ''
            passw = ''

            # Buscamos en la lista usuario por usuario si existe la cedula:
            for u in usuarios:
                # comprobamos el documento ingresado:
                # Si corresponde con el documento, es el usuario correcto:
                if u.documento == self.documento.text():
                    # Indicamos que encontramos el documento:
                    existeDocumento = True
                    #Guardamos las respuestas
                    resp1 = u.respuesta1
                    resp2 = u.respuesta2
                    resp3 = u.respuesta3
                    passw = u.password
                    # Paramos el for:
                    break

            # Verificamos si las respuestas son las correctas:
            # Hacemos que las respuestas sean en letra minuscula:
            if (
                    # usamos strip() para borrar espacios y saltos de linea:
                    self.respuesta1.text().lower().strip() == resp1.lower().strip() and
                    # usamos strip() para borrar espacios y saltos de linea:
                    self.respuesta2.text().lower().strip() == resp2.lower().strip() and
                    # usamos strip() para borrar espacios y saltos de linea:
                    self.respuesta3.text().lower().strip() == resp3.lower().strip()

            ):
                # Limpiamos los campos:
                self.accion_botonLimpiar()

                # Escribimos el texto explicativo
                self.mensaje.setText("Contraseña: " + passw)

                # Hacemos que la ventana de dialogo se vea:
                self.ventanaDialogo.exec_()
            else:
                # Escribimos el texto explicativo:
                self.mensaje.setText("Las respuestas son incorrectas para estas "
                                     "\npreguntas de recuperacion"
                                     "\nVuelva a intentarlo.")

                # Hacemos que la ventana de dialogo se vea
                self.ventanaDialogo.exec_()

    # Metodo del boton botonContinuar
    def accion_botonContinuar(self):
        self.hide()
        self.ventana2 = Ventana2(self)
        self.ventana2.show()





if __name__ == '__main__':
    app = QApplication(sys.argv)

    ventana1 = Ventana1()

    ventana1.show()

    sys.exit(app.exec_())















