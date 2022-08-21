from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QSizePolicy


class VistaLogin(QWidget):

    def __init__(self, parent=None):
        super(VistaLogin,self).__init__(parent)
        grid_layout=QGridLayout()
        grid_layout.addWidget(self.get_generic_button("Login", self.go_login),0,0)
        self.setLayout(grid_layout)
        grid_layout.addWidget(self.get_generic_button("Hai dimenticato la password?", self.go_lostpassword),0 ,1 )
        self.setLayout(grid_layout)


    def get_generic_button(self,titolo,on_click):
        button=QPushButton(titolo)
        button.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        button.clicked.connect(on_click)
        return button

    def go_login(self):
        self
        pass

    def go_lostpassword(self):
        self
        pass






