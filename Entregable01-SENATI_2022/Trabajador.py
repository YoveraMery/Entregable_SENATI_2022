class Trabajador:#Declare la clase principal named 'Trabajador'
    #Función para inicializar
    def __init__(self):
        self.worker = None
        self.category = None
        self.extrahours = None
        self.tardies = None
        
    print(f'''
---------------------------------------------
            FERROTEK S.A.C
---------------------------------------------''')
        
    def e_worker(self): #Entradas
        self.worker = input("Trabajador                  : ").upper() #Convierte una cadena a mayúsculas
        return self.worker
    
    def e_category(self):
        while True: #Bucle
            try: # Sentencias que quieres ejecutar, 
                self.category = input("Categoría [A | B | C]     : ").upper()
                if self.category == 'A' or self.category == 'B' or self.category == 'C':
                    break  # Si no da error, corto el while con break
                else:
                    print('Categoría Inválida')
            except ValueError:  #El bloque except se ejecutará cuando el bloque try falle. 
                print('Categoría Inválida')    
        return self.category
    
    def e_extrahours(self):
        while True:
            try:
                self.extrahours= int(input("Horas extras         : "))
                break  # Si no da error, corto el while con break
            except ValueError:
                print("Eso no es un número, prueba otra vez...")
        return self.extrahours    
    def e_tardies(self):
        while True:
            try:
                self.tardies= int(input("Tardanzas (minutos)     : "))
                break  # Si no da error, corto el while con break
            except ValueError:
                print("Eso no es un número, prueba otra vez...")            
        return self.tardies 
    
#Simplemente te está avisando de que aunque le asignas un valor a la variable, no usas después ese valor para nada.