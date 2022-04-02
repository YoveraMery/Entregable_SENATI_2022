from Trabajador import Trabajador #Importamos del archivo trabajador la clase Trabajador
from Boleta import Boleta  #Importamos del archivo Boleta la clase Boleta

#Métodos de la clase main
trabajador1= Trabajador()
trabajador1.e_worker()
category = trabajador1.e_category()
extrahours = trabajador1.e_extrahours()  
tardies = trabajador1.e_tardies()
boleta1=Boleta(category, extrahours, tardies)

def imprimir():
    print(f'''
--------------------------------------------------------
|            DATOS INGRESADOS DEL USUARIO
|--------------------------------------------------------
|Trabajador:    {trabajador1.worker}
|Categoría:     {trabajador1.category}
|Horas extras:  {trabajador1.extrahours}
|Tardanzas:     {trabajador1.tardies}
|------------------------------------------------------
|            ¡¡¡BIENVENIDO(A) {trabajador1.worker} !!!             
|------------------------------------------------------
|               BOLETA DE PAGO                         
|----------------------------------------------------             
|Trabajador          :   {trabajador1.worker}                
|Categoría           :   {trabajador1.category}              
|Sueldo Básico       : S/{boleta1.basic_salary()}        
|Descuentos Tardanzas: S/{boleta1.descontar_tarifa()}    
|Pago Horas extras   : S/{boleta1.calculate_phx()}       
|Sueldo Neto         : S/{boleta1.calcular_sueldoNeto()} 
|------------------------------------------------------
|                FERROTEK SAC                          |
|------------------------------------------------------|
''')
datos=imprimir()
