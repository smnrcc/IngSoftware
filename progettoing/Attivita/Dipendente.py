import os
import pickle

from Attivita.Utilizzatore import Utilzzatore

class Dipendente(Utilzzatore):

    def __init__(self):
        super().__init__()
        self.id = ""
        self.password= ""

    def aggiungiDipendente(self, id, password , codiceFiscale, cognome, dataNascita, email, nome, telefono, codice):
        self.aggiungiUtilizzatore(telefono=telefono, nome=nome, cognome =cognome, email=email, dataNascita=dataNascita,
                                  codiceFiscale=codiceFiscale, codice=codice)
        self.id=id
        self.password=password
        utilizzatori={}
        if os.path.isfile("Dati"):
            with open("Dati/Utiizzatori.pickle", "rb") as f:
                utilizzatori=pickle.load(f)
        utilizzatori[codice]=self
        with open("Dati/Utilizzatori.pickle", "wb") as f:
            pickle.dump(utilizzatori, f, pickle.HIGHEST_PROTOCOL)

    def getInfoDipendente(self):
        info= self.getinfoUtilizzatore()
        info["id"]= self.id
        info["password"]= self.password
        return info

    def ricercaUtilizzatoreCodiceFiscale(self, codiceFiscale):
        if os.path.isfile("Dati/Utilizzatori.pickle"):
            with open("Dati/Utilizzatori.pickle", "rb") as f:
                utilizzatori= dict(pickle.load(f))
                for utilizzatore in utilizzatori.values():
                    if utilizzatore.codiceFiscale == codiceFiscale
                        return utilizzatore
                return None
        else:
            return None













