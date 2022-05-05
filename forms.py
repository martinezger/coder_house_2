"""
COPIAR ESTE CODIGO EN forms.py
"""

import os
from datetime import datetime
from pathlib import Path


class FormPersona:
    """ Formulario Generico"""
    __path = "./info"

    def __init__(self, nombre, apellido, fecha_nacimiento, pais):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.pais = pais

    def __str__(self):
        return "form_generico" # esto define el nombre del archivo csv a crear.
    
    def validar_campos(self):
        if not self.nombre.isalpha():
            raise ValueError("Nombre tiene que ser Alfabético")
        
        if not self.apellido.isalpha():
            raise ValueError("Nombre tiene que ser Alfabético")
        try:
            datetime.strptime(self.fecha_nacimiento, "%d/%m/%Y")
        except ValueError:
            raise ValueError("El formato de la fecha no es correcto, formato valido DD/MM/AAAA")


    def guardar_formulario(self):
        file_path = os.path.join(self.__path, str(self)+".csv") #os.path.join, arma un string con la ruta al archivo. ej "./info/form_generico.csv"
        with open(file_path, "a+") as f: # a+ significa, append si existe el archivo o crear archivo y escribir si no existe.
            renglon = ",".join(self.__dict__.values()) + "\n" # armo un string separado por comas con los valores de mis atributos
            f.write(renglon)
        
        print(f"Registro guardado con éxito en {Path(file_path).resolve()}") # La clase Path recive un string y tiene un metodo resolve que muestra la ruta absoluta.



class FormUsuario(FormPersona):
    """ Formulario para carga de un nuevo usuario al sistema """

    def __init__(self, password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.password = password

    def __str__(self):
        return "form_usuario" # esto define el nombre del archivo csv a crear.

    def validar_campos(self):
        super().validar_campos()
 
        if len(self.password) < 7:
            raise ValueError("El password tiene que tener como mínimo 7 caracteres")
    


class FormIndiceMasaCorporal(FormPersona):
  """
  TODO (por hacer): Crear un formulario que pueda ser usado para guardar 
  los datos de Altura y Peso. Luego en Report cree un nuevo reporte para 
  que imprima el indice de masa corporal por persona.
  """
  pass
