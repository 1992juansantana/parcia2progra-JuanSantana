class Boligrafo:
    def __init__(self, color):
        self.capacidad_tinta_maxima = 100
        self.grosor_punta = None
        self.color = color
        self.cantidad_tinta = 80
        
        
    def set_grosor_punta(self, grosor):
        self.grosor_punta = grosor   
        
    def escribir(self, cantidad):
        if self.cantidad_tinta > 0:
            if cantidad <= self.cantidad_tinta:
                self.cantidad_tinta -= cantidad
                print(f"Escribiento {cantidad} unidades de tinta")
            else:
                print("No hay suficiente tinta para escribir esa cantidad") 
        else:
                print("No se puede escribir , la tinta se ha acabado")
    
    def recargar_tinta(self):
        self.cantidad_tinta = self.capacidad_tinta_maxima
        print("Tinta recargada al maximo.")
        
    def __str__(self):
        return (f"boligrafo de color: {self.color}, "   
                f"cantidad de tinta: {self.capacidad_tinta_maxima}, " 
                f"capacidad de la tinta: {self.capacidad_tinta_maxima}, " 
                f"grosor de punta: {self.grosor_punta}, ") 
        
if __name__ == "__main__":
    boligrafo1 = Boligrafo("azul")
    print(boligrafo1)
    boligrafo1.escribir(20)
    print(boligrafo1)
    boligrafo1.recargar_tinta()
    print(boligrafo1)   
