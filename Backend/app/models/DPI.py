class DPI:

    Bilan_biologique = []
    Compte_Rendus = []
    Hospitalisations = []
    Consultations = []

    def setId(self,id):
        self.id=id

    def setPatient(self,patient):
        self.patient=patient

    def addBilan_biologique(self,bilan):
        self.Bilan_biologique.append(bilan)

    def addCompte_randu(self,compte_rendu):
        self.Compte_Rendus.append(compte_rendu)

    def addHospitalisation(self,hospitalisaiton):
        self.Hospitalisations.append(hospitalisaiton)

    def addConsultation(self,consultation):
        self.Consultations.append(consultation)

