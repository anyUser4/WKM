#[Web Kit Medic (WKM); Configuración [Español]].
import os
import sys
import codecs
import pandas as pd
from colorama import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

init()
os.system('clear')
#[Corpus; Creación de clase principal].
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.intramed.net/contenidolista.asp?contenidotipoid=27'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        WKM = QToolBar()
        self.addToolBar(WKM)


        #[subCorpus; Botones de HUB].
        #{A; Botón de regreso de página}
        back_btn = QAction('Regresar', self)
        back_btn.triggered.connect(self.browser.back)
        WKM.addAction(back_btn)
        #{B; Botón de pasado de página}
        forward_btn = QAction('Siguiente', self)
        forward_btn.triggered.connect(self.browser.forward)
        WKM.addAction(forward_btn)
        #{C; Botón de recargado de página}
        reload_btn = QAction('Regresar', self)
        reload_btn.triggered.connect(self.browser.reload)
        WKM.addAction(reload_btn)


        #[subCorpus; Buscadores pre-definidos].
        #{A; Wikipedia}
        wikipedia_btn = QAction('[Buscador; Wikipedia]', self)
        wikipedia_btn.triggered.connect(self.wikipedia_lab)
        WKM.addAction(wikipedia_btn)
        #{B; Google}
        google_btn = QAction('[Buscador; Google]', self)
        google_btn.triggered.connect(self.google_lab)
        WKM.addAction(google_btn)


        #[subCorpus; Área de medicina].
        #{A; BioDigital}
        home_btn = QAction('[Medicina; Modelado 3D]', self)
        home_btn.triggered.connect(self.navigate_home)
        WKM.addAction(home_btn)
        #{B; Diccionario de medicina 1}
        dict1 = QAction('[Medicina; Diccionario 1]', self)
        dict1.triggered.connect(self.dict_site_1)
        WKM.addAction(dict1)
        #{C; Diccionario de medicina 2}
        dict2 = QAction('[Medicina; Diccionario 2]', self)
        dict2.triggered.connect(self.dict_site_2)
        WKM.addAction(dict2)
        #{D; Diccionario de medicina 3}
        dict3 = QAction('[Medicina; Diccionario 3]', self)
        dict3.triggered.connect(self.dict_site_3)
        WKM.addAction(dict3)
        #{E; Tabla periódica}
        tperi = QAction('[Química; Tabla periódica]', self)
        tperi.triggered.connect(self.periodicT)
        WKM.addAction(tperi)
        #{F; Calculadora de masa}
        cMass = QAction('[Química; Calculadora de masa]', self)
        cMass.triggered.connect(self.massCalc)
        WKM.addAction(cMass)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        WKM.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)


    #[subCorpus; Buscadores].
    #{A; Wikipedia}
    def wikipedia_lab(self):
        self.browser.setUrl(QUrl('https://es.wikipedia.org/wiki/Wikipedia:Portada'))
    #{B; Google}
    def google_lab(self):
        self.browser.setUrl(QUrl('https://www.google.com/?hl=es'))

    #[subCorpus; Funciones de opciones].
    #{A; Modelado 3D}
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://human.biodigital.com/explore'))
    #{B; Diccionario médico 1}
    def dict_site_1(self):
    	self.browser.setUrl(QUrl('https://dicciomed.usal.es/'))
    #{C; Diccionario médico 2}
    def dict_site_2(self):
        self.browser.setUrl(QUrl('https://dtme.ranm.es/index.aspx'))
    #{D; Diccionario médico 3}
    def dict_site_3(self):
        self.browser.setUrl(QUrl('https://www.hospitalaleman.org.ar/diccionario-medico/'))
    #{E; Tabla periódica}
    def periodicT(self):
        self.browser.setUrl(QUrl('https://atom.horuslugo.com/periodic-table'))
    #{F; Calculadora de masa}
    def massCalc(self):
        self.browser.setUrl(QUrl('https://atom.horuslugo.com/mass-calculator'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


#[Corpus; Pantalla de ejecución de programa].
print(Fore.GREEN + Style.BRIGHT)
print("[Web Kit Medic (WKM); Programa ejecutado correctamente].")

#[subCorpus; Configuración de variables].
"""
a1 = "Correo: "
a2 = "Contraseña:"

b1 = "eMail"
b2 = "pass"

print(Fore.CYAN + Style.BRIGHT)
print("[Lista de credenciales de acceso]")
s = pd.Series({a1:b1, a2:b2})
print(s)
"""

print(Fore.YELLOW + Style.BRIGHT)
print("[Consola; Registro de navegación (en tiempo real)]")

#[Corpus; Ejecución de programa].
app = QApplication(sys.argv)
QApplication.setApplicationName('Web Kit Medic (WKM) [V0.0.1]')
window = MainWindow()
app.exec_()