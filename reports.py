"""
COPIAR ESTE CODIGO EN reports.py
"""
import csv
from pathlib import Path


class ReportGenerico:
    """Reporte de Usuarios del sistema"""

    def __init__(self, path_archivo, nombre_reporte):
        self.path_archivo = path_archivo
        self.nombre_reporte = nombre_reporte
        self.cantidad_usuarios = 0
        self.usuarios_por_pais = {}

    def procesar(self):
        with open(self.path_archivo) as f:
            usuarios = csv.reader(f, delimiter=",")
            #en un solo for cuento cantidad de usuarios y saco cantidad por pais
            for renglon in usuarios:
                self.cantidad_usuarios += 1
                # el cuarto elemento en nuestro csv en pais
                self.usuarios_por_pais[renglon[3]] = self.usuarios_por_pais.get(renglon[3], 0) + 1

    def imprimir(self): 
        print(f"{self.nombre_reporte}\n")
        print ("{:<20} {}\n".format('Pais','Cantidad'))
        for k,v in self.usuarios_por_pais.items():
            print("{:<20} {}".format(k, v))
        print(f"\ntotal:{self.cantidad_usuarios}")


class ReportConColores(ReportGenerico):
    
    # codigos ansi para formatear texto impreso por pantalla 
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def imprimir(self):
        print(f"{self.UNDERLINE}{self.HEADER}{self.nombre_reporte}{self.ENDC}\n")
        print ("{:<20} {}\n".format('Pais','Cantidad Usuarios'))
        for k,v in self.usuarios_por_pais.items():
            print("{:<20} {}".format(k, v))

        print(f"\n{self.BOLD}{self.OKGREEN}Total: {self.cantidad_usuarios}")


class ReportEdad(ReportGenerico): 
  """
  TODO (por hacer): Codifique un reporte que calcule la edad de cada usuario
  
  salida esperada:

  Reporte: Edades de Usuario
  
  Nombre    Apellido  Edad  Fecha Nacimiento
  German    Martinez  35    06/03/1987
  Claudia   Galarza   49    20/05/1972      

  Prom Edad Usuarios: 42
  """
  pass

class reportIndiceMasaCorporal(ReportGenerico):
  """
  TODO (por hacer): Codifique un reporte que imprima por pantalla el indice
  de masa corporal por cada persona ingresada.

  salida esperada:

  Reporte: IMC de Personas
  
  Nombre    Apellido  Edad  Fecha Nacimiento      IMC
  German    Martinez  35    06/03/1987            24.9
  Claudia   Galarza   49    20/05/1972            23.6   
  Sofia     Terada    33    25/06/1986            22.4   

  Persona con IMC mas alto: German Martinez
  Persona con IMC mas bajo: Sofia Terada
  Promedio IMC: 23.64
  """
  pass