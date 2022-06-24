import datetime
from abc import abstractmethod


class Utilzzatore:


    def __init__(self):
        self.codice =-1
        self.codiceFiscale = ""
        self.cognome= ""
        self.dataNascita=  datetime.datetime(year=1970, month =1, day= 1)
        self.email= ""
        self.nome = ""
        self.telefono= 0

    def aggiungiUtilizzatore(self,codice, codiceFiscale, cognome, dataNascita, email, nome, telefono):
        self.codice = codice
        self.codiceFiscale = codiceFiscale
        self.cognome =  cognome
        self.dataNascita = dataNascita
        self.email = email
        self.nome = nome
        self.telefono = telefono

    def getinfoUtilizzatore(self):
        return{
            "codice": self.codice,
            "codiceFiscale": self.codiceFiscale,
            "cognome": self.cognome,
            "dataNascita": self.dataNascita,
            "email": self.email,
            "nome": self.nome,
            "telefono": self.telefono
        }

    @abstractmethod
    def ricercaUtilizzatore(self,nome, cognome):
         pass

    @abstractmethod
    def ricercaUtilizzatore(self,codiceFiscale):
         pass

    @abstractmethod
    def ricercaUtilizzatore(self,codice):
         pass

    def rimuoviUtilizzatore(self):
         self.codice = -1
         self.codiceFiscale = ""
         self.cognome = ""
         self.dataNascita = datetime.datetime(year=1970, month=1, day=1)
         self.email = ""
         self.nome = ""
         self.telefono = 0

