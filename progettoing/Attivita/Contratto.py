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


