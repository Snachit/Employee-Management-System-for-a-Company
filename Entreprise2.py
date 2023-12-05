class Employe:
    def __init__(self, nom, poste, salaire):
        self.nom = nom 
        self.poste = poste
        self.salaire = salaire 

    def Augmenter_salaire(self, pourcentage):
        return self.salaire + (self.salaire * pourcentage) / 100
    
class Departement:
    def __init__(self, nom):
        self.nom = nom
        self.liste_employe = []

    def Ajouter_Employer(self, employe):
        self.liste_employe.append(employe)

    def Afficher_employes(self):
        print(f"Departement {self.nom}")
        print("Liste d employe : ")
        for employe in self.liste_employe:
            print(f"-Nom:{employe.nom} -Poste:{employe.poste} -Salaire:{employe.salaire} DH")

class Entreprise:
    def __init__(self, nom):
        self.nom = nom 
        self.liste_entreprise = []

    def Ajouter_departement(self, departement):
        self.liste_entreprise.append(departement)

    def Afficher_departements(self):
        print(f"-------------------------------------------Entreprise {self.nom}-------------------------------------------")
        print("")
        for departement in self.liste_entreprise:
            departement.Afficher_employes()
            print("")

emp = Employe("Amin", "Directeur General", 15000)
emp1 = Employe("Salma", "femme de menage", 3000)
depar = Departement("CHABKA")
depar.Ajouter_Employer(emp)
depar.Ajouter_Employer(emp1)

emp2 = Employe("Kamal", "Responsable financiaire", 20000)
emp3 = Employe("Amina", "Responsable femme de menage", 3500)
depar1 = Departement("Sabona")
depar1.Ajouter_Employer(emp2)
depar1.Ajouter_Employer(emp3)

entreprise = Entreprise("Lharara")
entreprise.Ajouter_departement(depar)
entreprise.Ajouter_departement(depar1)
entreprise.Afficher_departements()
