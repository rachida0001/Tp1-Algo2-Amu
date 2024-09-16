#Nom : Guedouari Rachida

class Vecteur:
    def __init__(self, coeffs):
        print("Creation d'une instance de Vecteur")
        self.v = list(coeffs)
        
    def dimension(self):
        """Renvoie la dimension du vecteur"""
        return len(self.v)
    
    def get(self, i):
        """Renvoie le coefficient d'indice i"""
        return self.v[i]
    
    def afficher(self):
        """Affiche les coefficients du vecteur sous la forme [coeff1 ; coeff2 ; ...]"""
        mes = "["
        for i in range(self.dimension()):
            mes = mes + str(self.v[i]) + ";"
        print(mes[:-1]+ "]")
        
    def somme(self,vec2):
        """Calcule la somme de deux vecteurs si leur dimension est la même"""   
        if self.dimension() != vec2.dimension():
            raise ValueError("Les vecteurs doivent avoir la meme dimension")
        return Vecteur([self.get(i) + vec2.get(i) for i in range(self.dimension())])



class Polynome(Vecteur):
    def __init__(self, coeffs):
        super().__init__(coeffs)
    
    def degre(self):
        """Renvoie le degré du polynôme"""
        return self.dimension() -1
    
    def afficher(self):
        """Affiche le polynôme sous la forme coeff0 x^0 + coeff1 x^1 + ..."""
        mes = ""
        for i in range(self.dimension()):
            mes = mes + str(self.v[i]) + "x^" + str(i) + "+"   
        print(mes[:-1])
    
    def somme(self, vec2):
        """Calcule la somme de deux polynomes"""   
        s = []
        for i in range(max(self.dimension(), vec2.dimension())):
            if (min(self.degre(), vec2.degre()) >= i):
                s.append(self.get(i) + vec2.get(i))
            else:
                if(self.dimension()>vec2.dimension()):
                    s.append(self.get(i))
                else:
                    s.append(vec2.get(i))
        return Polynome(s)
    
    def evaluer(self , x):
        """Évalue le polynôme en utilisant la méthode de Horner"""
        resultat = 0
        for i in range(len(self.v)-1, -1, -1):
            resultat = self.v[i] + (x * resultat)
        return resultat
        
if __name__ == "__main__":

    # Création de quelques vecteurs pour tester
    v1 = Vecteur([10, 20])
    v2 = Vecteur((5, -2, 1.5))
    v3 = Vecteur(range(4, 8))
    
    # On affiche les vecteurs pour voir si tout est correct
    print("Affichage de v1, v2 et v3:")
    v1.afficher() 
    v2.afficher()  
    v3.afficher()  

    # Vérifions les dimensions
    print(f"Dimension de v1: {v1.dimension()}")  
    print(f"Dimension de v2: {v2.dimension()}")  

    # Test de la methode get(i)
    print(f"Coefficient d'indice 1 de v1: {v1.get(1)}")  

    # Test de la somme de deux vecteurs de dimension differentes 
    #v4 = v1.somme(v2)  #Resultat : ValueError: Les vecteurs doivent avoir la meme dimension

    # Test de la somme de deux vecteurs 
    v5 = Vecteur([1, 3])
    v6 = v1.somme(v5)
    v6.afficher() 

    # Créons quelques polynômes
    p1 = Polynome([2, 3, 4])  
    p2 = Polynome([1, -1, 1])  

    # Test de l'affichage des polynômes
    print("Affichage des polynômes:")
    p1.afficher()  
    p2.afficher()  

    # Test du degré des polynômes
    print("Degré des polynômes:")
    print(f"Degré de p1: {p1.degre()}")  
    print(f"Degré de p2: {p2.degre()}")  

    # Test de la somme de deux vecteurs
    print("Somme de deux polynômes:")
    v7 = v1.somme(v5)
    v7.afficher() 
    print("Type de la somme de deux vecteurs",type(v7)) 

    # Test de la somme de deux polynômes
    print("Somme de deux polynômes:")
    p3 = p1.somme(p2)
    p3.afficher() 
    print("Type de la somme de deux Polynomes",type(p3)) 

    # Test de l'évaluation d'un polynôme pour une valeur donnée de x
    x = 2
    print(f"Valeur de p1 pour x = {x}: {p1.evaluer(x)}")  
    
    
    
    # Test de la methode dimension 
    print("Dimension de v1 est",v1.dimension())
    print("Dimension de v2 est",v2.dimension())
    print("Dimension de v3 est",v3.dimension())