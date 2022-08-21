import sys

from PyQt5.QtWidgets import QApplication

from Viste.VistaLogin import VistaLogin

if __name__ == '__main__':
   
   app= QApplication(sys.argv)
   vista_login = VistaLogin()
   vista_login.show()
   sys.exit(app.exec())

