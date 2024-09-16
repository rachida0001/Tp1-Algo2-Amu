class Vecteur:
    def __init__(self, coeffs):
        print("Creation d'une instance de Vecteur")
        self.v = list(coeffs)
        
    def dimension(self):
        return len(self.v)
    
    def get(self, i):
        return self.v[i]
    
    def afficher(self):
        mes = "["
        for i in range(self.dimension()):
            mes = mes + str(self.v[i]) + ";"
        print(mes[:-1]+ "]")
        
    def somme(self,vec2):
            
        if self.dimension() != vec2.dimension():
            raise ValueError("Les vecteurs doivent avoir la meme dimension")
        s = [self.get(i) + vec2.get(i) for i in range(self.dimension())]
        
        if isinstance(self, Polynome):
            return Polynome((s))
        return Vecteur(s)

    def somme_2(self, vec2):
        if isinstance(self, Polynome):
            s = []
            for i in range(max(self.dimension(), vec2.dimension())):
                if (min(self.degree(), vec2.degree()) >= i):
                    s.append(self.get(i) + vec2.get(i))
                else:
                    if(self.dimension()>vec2.dimension()):
                        s.append(self.get(i))
                    else:
                        s.append(vec2.get(i))
            return Polynome(s)
        else:
            if self.dimension() != vec2.dimension():
                raise ValueError("Les vecteurs doivent avoir la meme dimension")
            s = [self.get(i) + vec2.get(i) for i in range(self.dimension())]
            return Vecteur(s)
    

class Polynome(Vecteur):
    def __init__(self, coeffs):
        super().__init__(coeffs)
    
    def degree(self):
        return self.dimension() -1
    
    def afficher(self):
        mes = ""
        for i in range(self.dimension()):
            mes = mes + str(self.v[i]) + "x^" + str(i) + "+"   
        print(mes[:-1])
    
    def evaluer(self , x):
        result = 0
        for i in range(len(self.v)-1, -1, -1):
            result = self.v[i] + (x * result)
            print(result)
        return result
        
if __name__ == "__main__":
    
    v1 = Vecteur([1,7])
    v2 = Vecteur((5, -2, 1.5))
    v3 = Vecteur(range(4,8))
    
    # Test de la methode dimension 
    print("Dimension de v1 est",v1.dimension())
    print("Dimension de v2 est",v2.dimension())
    print("Dimension de v3 est",v3.dimension())
    
    p1 = Polynome([1,2])
    p2 = Polynome([1,1,1])
    
    v4 = Vecteur([1,1,1])
    v5 = v2.somme(v4)
    print(type(v5))
    
    p3 = p1.somme_2(p2)
    p3.afficher()
    print(type(p3))