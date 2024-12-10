class Hospitalisation:

    def __init__(self):
        self.Decompte_des_frais = None
        self.id = None
        self.Soins = []

    def setId(self,id):
        self.id = id

    def addDecompte_Des_Frais(self,frais):
        self.Decompte_des_frais = frais

    def addSoins(self,soin):
        self.Soins.append(soin)

