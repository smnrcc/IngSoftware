import os
import pickle

from Attivita.Utilizzatore import Utilzzatore

class Dipendente(Utilzzatore):

    def __init__(self):
        super().__init__()
        self.noleggio=[]
        self.note=""

    def aggiungiCliente(self, noleggio, note , codiceFiscale, cognome, dataNascita, email, nome, telefono, codice):
        self.aggiungiUtilizzatore(telefono=telefono, nome=nome, cognome =cognome, email=email, dataNascita=dataNascita,
                                  codiceFiscale=codiceFiscale, codice=codice)
        self.noleggio=noleggio
        self.note=note
        clienti={}
        if os.path.isfile("Dati/Clienti.pickle"):
            with open("Dati/Clienti.pickle", "rb") as f:
                clienti=pickle.load(f)
        clienti[codice]=self
        with open("Dati/Clienti.pickle", "wb") as f:
            pickle.dump(clienti, f, pickle.HIGHEST_PROTOCOL)

    def getInfoCliente(self):
        info= self.getinfoUtilizzatore()
        info["noleggio"]= self.noleggio
        info["note"]= self.note
        return info

    def ricercaUtilizzatoreCodiceFiscale(self, codiceFiscale):
        if os.path.isfile("Dati/Clienti.pickle"):
            with open("Dati/Clienti.pickle", "rb") as f:
                clienti= dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.codiceFiscale == codiceFiscale:
                        return cliente
                return None
        else:
            return None

    def ricercaUtilizzatoreNomeCognome(self,nome,cognome):
        if os.path.isfile("Dati/Cliente.pickle"):
            with open("Dati/Cliente.pickle", "rb") as f:
                clienti= dict(pickle.load(f))
                for cliente in clienti.values():
                    if cliente.nome==nome and cliente.cognome==cognome:
                        return cliente
                    return None
        else:
            return None

    def ricercaUtilizzatore(self,codice):
        if os.path.isfile("Dati/Clienti.pickle"):
            with open("Dati/Clienti.picke", "rb") as f:
                clienti= dict(pickle.load(f))
                try:
                    return clienti[codice]
                except:
                    return None
        else:
            return None

    def rimuoviCliente(self):
        if os.path.isfile("Dati/Clienti.pickle"):
            with open("Dati/Clienti.pickle", "rb") as f:
                clienti= pickle.load(f)
                del clienti[self.codice]
            with open("Dati/Clienti.pickle", "wb") as f:
             pickle.dump(clienti, f , pickle.HIGHEST_PROTOCOL)
        self.rimuoviUtilizzatore()
        self.noleggio = []
        self.note = ""
        del self













