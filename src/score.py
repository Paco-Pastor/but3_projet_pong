# implémenter classe Score
# un objet score pour chaque joueur
# mettre à jour attribut score au fur et à mesure de la partie
class Score:
    def __init__(self):
        self.score = 0
    def update(self):
        self.score += 1
    def get(self):
        return self.score


