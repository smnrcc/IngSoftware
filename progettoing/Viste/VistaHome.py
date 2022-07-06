from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaHome(QWidget):

    def __init__(self, parent=None):
        super(VistaHome,self).__init__(parent)
        grid_layout=QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Login", self.go_servizi),0,0)
        self.setLayout(grid_layout)


    def get_generic_button(self,titolo,on_click):
        button=QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_dipendente(self):
        self.
        pass






