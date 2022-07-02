import datetime
import os
import pickle
from Attivita import Cliente
class Pagamento (Cliente):
    def __init__(self):
        self.numeroCarta= (16,"")
        self.scadenzaCarta= datetime.datetime(1,1970)
        self.cvv= ""
        self.intestatario=""

    def aggiungiCarta(self, numeroCarta, scadenzaCarta, cvv, intestatario):
        self.numeroCarta=numeroCarta
        self.scadenzaCarta=scadenzaCarta
        self.cvv=cvv
        self.intestatario=intestatario

    def getInfoPagamento(self):
        info= self.getinfoUtilizzatore()
        info["numeroCarta"]= self.numeroCarta
        info["scadenzaCarta"]= self.scadenzaCarta
        info["cvv"]=self.cvv
        info["intestatario"]=self.intestatario
        return info

    def ricercaCarta(self, intestatario):
        if os.path.isfile("Dati/Carta.pickle"):
            with open("Dati/Carta.pickle", "rb") as f:
                carta=dict(pickle.load(f))
                for carte  in carta.values():
                    if carta.intestatario==intestatario:
                        return carta
                return None
        else:
            return None

    def rimuoviCarta(self):
        if os.path.isfile("Dati/Carta.pickle"):
            with open("Dati/Carta.pickle", "rb") as f:
                carta = pickle.load(f)
                del carta[self.intestatario]
            with open("Dati/Carta.pickle", "wb") as f:
                pickle.dump(carta,f, pickle.HIGHEST_PROTOCOL)
        self.rimuoviCarta()
        self.numeroCarta = ""
        self.scadenzaCarta = datetime.datetime(1, 1970)
        self.cvv = ""
        self.intestatario = ""
        del self



