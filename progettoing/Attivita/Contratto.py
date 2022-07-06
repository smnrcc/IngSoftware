import datetime
class Contratto:
    def __init__(self):
        self.dataRilascio = datetime.datetime(1970,1,1,0,0)
        self.prezzoIngresso=0.0
        self.prezzoUscita=0.0
        self.tipoVeicolo=""
        self.accessori=""
        self.codice=0
        self.dataScadenza= datetime.datetime(1970,1,1,0,0)
        self.assicurazione=False

    def aggiungiContratto(self, dataRilascio, prezzoIngresso, prezzoUscita, tipoVeicolo, accessori, codice, dataScadenza, assicurazione):
        self.dataRilascio=dataRilascio
        self.prezzoUscita=prezzoUscita
        self.prezzoIngresso=prezzoIngresso
        self.tipoVeicolo=tipoVeicolo
        self.accessori=accessori
        self.codice=codice
        self.dataScadenza=dataScadenza
        self.assicurazione=assicurazione

